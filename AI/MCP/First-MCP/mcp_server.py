#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP (Model Context Protocol) 服务器示例

这个示例演示了如何使用Python创建一个简单的MCP服务器，
提供工具和资源供MCP客户端调用。
"""

import asyncio
import json
import websockets
import uuid
from datetime import datetime
from typing import Dict, Any, List


class MCPServer:
    """
    简单的MCP服务器实现
    """
    
    def __init__(self):
        """
        初始化MCP服务器
        """
        self.tools = self._init_tools()
        self.resources = self._init_resources()
        self.clients = {}
        
    def _init_tools(self) -> List[Dict[str, Any]]:
        """
        初始化服务器支持的工具
        
        Returns:
            工具列表
        """
        return [
            {
                "name": "calculator",
                "description": "执行数学计算",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string", 
                            "description": "数学表达式，例如: 2 + 3 * 4"
                        }
                    },
                    "required": ["expression"]
                }
            },
            {
                "name": "get_weather",
                "description": "获取指定城市的天气信息",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string", 
                            "description": "城市名称，例如: 北京"
                        }
                    },
                    "required": ["city"]
                }
            }
        ]
    
    def _init_resources(self) -> List[Dict[str, Any]]:
        """
        初始化服务器提供的资源
        
        Returns:
            资源列表
        """
        return [
            {
                "uri": "file://README.md",
                "name": "项目说明",
                "description": "项目的README文件",
                "mimeType": "text/markdown"
            },
            {
                "uri": "file://data/users.json",
                "name": "用户数据",
                "description": "系统中的用户信息",
                "mimeType": "application/json"
            }
        ]
    
    async def handle_client(self, websocket, path):
        """
        处理客户端连接
        
        Args:
            websocket: WebSocket连接
            path: 请求路径
        """
        client_id = str(uuid.uuid4())
        self.clients[client_id] = websocket
        print(f"新客户端连接: {client_id}")
        
        try:
            async for message in websocket:
                await self.process_message(client_id, message)
        except websockets.exceptions.ConnectionClosed:
            print(f"客户端断开连接: {client_id}")
        finally:
            del self.clients[client_id]
    
    async def process_message(self, client_id: str, message: str):
        """
        处理客户端消息
        
        Args:
            client_id: 客户端ID
            message: 接收到的消息
        """
        try:
            data = json.loads(message)
            method = data.get("method")
            msg_id = data.get("id")
            
            print(f"收到来自 {client_id} 的消息: {method}")
            
            if method == "initialize":
                await self.handle_initialize(client_id, msg_id, data.get("params", {}))
            elif method == "tools/list":
                await self.handle_list_tools(client_id, msg_id)
            elif method == "tools/call":
                await self.handle_call_tool(client_id, msg_id, data.get("params", {}))
            elif method == "resources/list":
                await self.handle_list_resources(client_id, msg_id)
            elif method == "resources/read":
                await self.handle_read_resource(client_id, msg_id, data.get("params", {}))
            else:
                await self.send_error(client_id, msg_id, f"未知方法: {method}")
        except json.JSONDecodeError:
            await self.send_error(client_id, None, "无效的JSON格式")
        except Exception as e:
            await self.send_error(client_id, None, str(e))
    
    async def handle_initialize(self, client_id: str, msg_id: str, params: Dict[str, Any]):
        """
        处理初始化请求
        
        Args:
            client_id: 客户端ID
            msg_id: 消息ID
            params: 请求参数
        """
        response = {
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-01-01",
                "capabilities": {
                    "tools": {},
                    "resources": {}
                }
            }
        }
        await self.send_response(client_id, response)
    
    async def handle_list_tools(self, client_id: str, msg_id: str):
        """
        处理工具列表请求
        
        Args:
            client_id: 客户端ID
            msg_id: 消息ID
        """
        response = {
            "id": msg_id,
            "result": {
                "tools": self.tools
            }
        }
        await self.send_response(client_id, response)
    
    async def handle_call_tool(self, client_id: str, msg_id: str, params: Dict[str, Any]):
        """
        处理工具调用请求
        
        Args:
            client_id: 客户端ID
            msg_id: 消息ID
            params: 请求参数
        """
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        print(f"调用工具: {tool_name}，参数: {arguments}")
        
        result = None
        is_error = False
        
        if tool_name == "calculator":
            try:
                # 注意：在生产环境中，应该使用更安全的表达式解析器
                expression = arguments.get("expression", "")
                result_value = eval(expression)
                result = {"result": result_value}
            except Exception as e:
                result = {"error": f"计算错误: {str(e)}"}
                is_error = True
        elif tool_name == "get_weather":
            city = arguments.get("city", "未知城市")
            # 模拟天气数据
            result = {
                "city": city,
                "temperature": 25,
                "condition": "晴朗",
                "humidity": 60
            }
        else:
            result = {"error": f"未知工具: {tool_name}"}
            is_error = True
        
        response = {
            "id": msg_id,
            "result": result if not is_error else None,
            "error": result if is_error else None
        }
        await self.send_response(client_id, response)
    
    async def handle_list_resources(self, client_id: str, msg_id: str):
        """
        处理资源列表请求
        
        Args:
            client_id: 客户端ID
            msg_id: 消息ID
        """
        response = {
            "id": msg_id,
            "result": {
                "resources": self.resources
            }
        }
        await self.send_response(client_id, response)
    
    async def handle_read_resource(self, client_id: str, msg_id: str, params: Dict[str, Any]):
        """
        处理读取资源请求
        
        Args:
            client_id: 客户端ID
            msg_id: 消息ID
            params: 请求参数
        """
        uri = params.get("uri", "")
        
        print(f"读取资源: {uri}")
        
        content = ""
        if uri == "file://README.md":
            content = "# MCP 示例项目\n\n这是一个使用Python实现的MCP服务器示例。"
        elif uri == "file://data/users.json":
            content = json.dumps([
                {"id": 1, "name": "张三", "email": "zhangsan@example.com"},
                {"id": 2, "name": "李四", "email": "lisi@example.com"}
            ], ensure_ascii=False)
        else:
            error_response = {
                "id": msg_id,
                "error": {"message": f"未找到资源: {uri}"}
            }
            await self.send_response(client_id, error_response)
            return
        
        response = {
            "id": msg_id,
            "result": {
                "contents": [{"text": content}]
            }
        }
        await self.send_response(client_id, response)
    
    async def send_response(self, client_id: str, response: Dict[str, Any]):
        """
        发送响应给客户端
        
        Args:
            client_id: 客户端ID
            response: 响应数据
        """
        if client_id in self.clients:
            await self.clients[client_id].send(json.dumps(response, ensure_ascii=False))
    
    async def send_error(self, client_id: str, msg_id: str, message: str):
        """
        发送错误信息给客户端
        
        Args:
            client_id: 客户端ID
            msg_id: 消息ID
            message: 错误信息
        """
        error_response = {
            "id": msg_id,
            "error": {"message": message}
        }
        await self.send_response(client_id, error_response)


async def main():
    """
    主函数，启动MCP服务器
    """
    server = MCPServer()
    
    print("启动MCP服务器...")
    print("服务器地址: ws://localhost:8765")
    print("按 Ctrl+C 停止服务器")
    
    try:
        async with websockets.serve(server.handle_client, "localhost", 8765):
            await asyncio.Future()  # 运行直到被中断
    except KeyboardInterrupt:
        print("\n服务器已停止")


if __name__ == "__main__":
    asyncio.run(main())