#!/usr/bin/env python3

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # 配置服务器参数
    server_params = StdioServerParameters(
        command="python3",
        args=["server.py"],
        cwd="."
    )
    
    # 创建客户端连接
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化连接
            await session.initialize()
            
            # 列出可用工具
            print("Available tools:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")
            
            # 测试生成ASCII艺术字
            print("\n" + "="*50)
            print("Testing ASCII Art Generation")
            print("="*50)
            
            # 调用generate_ascii_art工具
            try:
                result = await session.call_tool("generate_ascii_art", {"text": "HELLO"})
                print("Result for 'HELLO':")
                print(result.content)
            except Exception as e:
                print(f"Error calling generate_ascii_art: {e}")
            
            print("\n" + "-"*30)
            
            # 调用generate_simple_ascii_art工具
            try:
                result = await session.call_tool("generate_simple_ascii_art", {"text": "MCP"})
                print("Result for 'MCP':")
                print(result.content)
            except Exception as e:
                print(f"Error calling generate_simple_ascii_art: {e}")

if __name__ == "__main__":
    asyncio.run(main())