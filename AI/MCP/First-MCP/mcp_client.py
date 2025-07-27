#!/usr/bin/env python3
"""
MCP (Model Context Protocol) 客户端示例

这个示例演示了如何使用Python创建一个简单的MCP客户端，
连接到MCP服务器并调用其提供的工具和资源。
"""

import asyncio
import json
import websockets
import uuid
from typing import Dict, Any, List


class MCPClient:
    """
    简单的MCP客户端实现
    """
    
    def __init__(self, server_uri: str = "ws://localhost:8765"):
        """
        初始化MCP客户端
        
        Args:
            server_uri: 服务器地址
        """
        self.server_uri = server_uri
        self.websocket = None
        self.msg_id_counter = 0
        self.pending_requests = {}
    
    async def connect(self):
        """
        连接到MCP服务器
        """
        print(f"正在连接到服务器: {self.server_uri}")
        self.websocket = await websockets.connect(self.server_uri)
        print("连接成功!")
    
    async def disconnect(self):
        """
        断开与服务器的连接
        """
        if self.websocket:
            await self.websocket.close()
            print("已断开连接")
    
    def _get_next_id(self) -> str:
        """
        获取下一个消息ID
        
        Returns:
            消息ID
        """
        self.msg_id_counter += 1
        return str(self.msg_id_counter)
    
    async def send_request(self, method: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        发送请求到服务器
        
        Args:
            method: 方法名
            params: 参数
            
        Returns:
            服务器响应
        """
        msg_id = self._get_next_id()
        request = {
            "id": msg_id,
            "method": method,
            "params": params or {}
        }
        
        # 创建future用于等待响应
        future = asyncio.Future()
        self.pending_requests[msg_id] = future
        
        # 发送请求
        await self.websocket.send(json.dumps(request, ensure_ascii=False))
        print(f"发送请求: {method}")
        
        # 等待响应
        return await future
    
    async def listen_for_responses(self):
        """
        监听服务器响应
        """
        try:
            async for message in self.websocket:
                data = json.loads(message)
                msg_id = data.get("id")
                
                if msg_id in self.pending_requests:
                    # 完成对应的future
                    future = self.pending_requests.pop(msg_id)
                    future.set_result(data)
        except websockets.exceptions.ConnectionClosed:
            print("与服务器的连接已关闭")
    
    async def initialize(self) -> Dict[str, Any]:
        """
        初始化与服务器的连接
        
        Returns:
            初始化结果
        """
        response = await self.send_request("initialize", {
            "protocolVersion": "2024-01-01",
            "clientInfo": {
                "name": "MCP Python Demo Client",
                "version": "1.0.0"
            }
        })
        
        if "result" in response:
            print(f"初始化成功，协议版本: {response['result']['protocolVersion']}")
        else:
            print(f"初始化失败: {response.get('error', '未知错误')}")
            
        return response
    
    async def list_tools(self) -> List[Dict[str, Any]]:
        """
        获取服务器支持的工具列表
        
        Returns:
            工具列表
        """
        response = await self.send_request("tools/list")
        
        if "result" in response:
            tools = response["result"]["tools"]
            print(f"获取到 {len(tools)} 个工具:")
            for i, tool in enumerate(tools, 1):
                print(f"  {i}. {tool['name']}: {tool['description']}")
            return tools
        else:
            print(f"获取工具列表失败: {response.get('error', '未知错误')}")
            return []
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        调用服务器上的工具
        
        Args:
            tool_name: 工具名称
            arguments: 工具参数
            
        Returns:
            工具调用结果
        """
        response = await self.send_request("tools/call", {
            "name": tool_name,
            "arguments": arguments
        })
        
        if "result" in response:
            print(f"工具 '{tool_name}' 调用成功:")
            print(json.dumps(response["result"], indent=2, ensure_ascii=False))
            return response["result"]
        else:
            print(f"工具 '{tool_name}' 调用失败:")
            print(json.dumps(response["error"], indent=2, ensure_ascii=False))
            return response["error"]
    
    async def list_resources(self) -> List[Dict[str, Any]]:
        """
        获取服务器提供的资源列表
        
        Returns:
            资源列表
        """
        response = await self.send_request("resources/list")
        
        if "result" in response:
            resources = response["result"]["resources"]
            print(f"获取到 {len(resources)} 个资源:")
            for i, resource in enumerate(resources, 1):
                print(f"  {i}. {resource['name']}: {resource['description']}")
            return resources
        else:
            print(f"获取资源列表失败: {response.get('error', '未知错误')}")
            return []
    
    async def read_resource(self, uri: str) -> str:
        """
        读取指定资源的内容
        
        Args:
            uri: 资源URI
            
        Returns:
            资源内容
        """
        response = await self.send_request("resources/read", {
            "uri": uri
        })
        
        if "result" in response:
            contents = response["result"]["contents"]
            if contents and "text" in contents[0]:
                content = contents[0]["text"]
                print(f"读取资源 '{uri}' 成功:")
                print("--- 资源内容开始 ---")
                print(content)
                print("--- 资源内容结束 ---")
                return content
        else:
            print(f"读取资源 '{uri}' 失败: {response.get('error', '未知错误')}")
        
        return ""


async def run_demo():
    """
    运行MCP客户端演示
    """
    print("=== MCP (Model Context Protocol) 客户端演示 ===\n")
    
    client = MCPClient()
    
    try:
        # 连接到服务器
        await client.connect()
        
        # 启动监听响应的任务
        listen_task = asyncio.create_task(client.listen_for_responses())
        
        # 初始化连接
        await client.initialize()
        
        # 获取工具列表
        print("\n--- 获取工具列表 ---")
        tools = await client.list_tools()
        
        # 调用计算器工具
        print("\n--- 调用计算器工具 ---")
        await client.call_tool("calculator", {
            "expression": "10 + 5 * 2"
        })
        
        # 调用天气查询工具
        print("\n--- 调用天气查询工具 ---")
        await client.call_tool("get_weather", {
            "city": "北京"
        })
        
        # 获取资源列表
        print("\n--- 获取资源列表 ---")
        resources = await client.list_resources()
        
        # 读取资源
        if resources:
            print("\n--- 读取第一个资源 ---")
            await client.read_resource(resources[0]["uri"])
            
            if len(resources) > 1:
                print("\n--- 读取第二个资源 ---")
                await client.read_resource(resources[1]["uri"])
        
        # 等待一段时间以确保所有消息都被处理
        await asyncio.sleep(1)
        
        # 断开连接
        listen_task.cancel()
        await client.disconnect()
        
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        print("\n=== 演示结束 ===")


async def main():
    """
    主函数
    """
    try:
        await run_demo()
    except KeyboardInterrupt:
        print("\n客户端已停止")


if __name__ == "__main__":
    asyncio.run(main())