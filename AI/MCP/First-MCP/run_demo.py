#!/usr/bin/env python3
"""
MCP (Model Context Protocol) 演示运行脚本

这个脚本提供了一种简单的方式来运行MCP服务器和客户端演示。
"""

import asyncio
import subprocess
import sys
import time
import os


def install_dependencies():
    """安装项目依赖"""
    print("检查并安装项目依赖...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("依赖安装完成!")
    except subprocess.CalledProcessError as e:
        print(f"依赖安装失败: {e}")
        sys.exit(1)


def start_server():
    """启动MCP服务器"""
    print("启动MCP服务器...")
    server_process = subprocess.Popen([sys.executable, "mcp_server.py"], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE,
                                    text=True)
    return server_process


def start_client():
    """启动MCP客户端"""
    print("启动MCP客户端...")
    client_process = subprocess.Popen([sys.executable, "mcp_client.py"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
    return client_process


async def main():
    """主函数"""
    print("=== MCP (Model Context Protocol) 演示运行脚本 ===\n")
    
    # 安装依赖
    install_dependencies()
    
    # 启动服务器
    server_process = start_server()
    print("服务器已启动，等待几秒钟...")
    time.sleep(3)  # 给服务器一些启动时间
    
    # 检查服务器是否仍在运行
    if server_process.poll() is not None:
        print("服务器启动失败!")
        stdout, stderr = server_process.communicate()
        print("服务器输出:")
        print(stdout)
        print("服务器错误:")
        print(stderr)
        return
    
    print("服务器运行正常\n")
    
    # 启动客户端
    client_process = start_client()
    
    # 等待客户端完成
    stdout, stderr = client_process.communicate()
    
    print("\n客户端输出:")
    print(stdout)
    
    if stderr:
        print("客户端错误:")
        print(stderr)
    
    # 停止服务器
    print("停止服务器...")
    server_process.terminate()
    try:
        server_process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        server_process.kill()
    
    print("演示完成!")


if __name__ == "__main__":
    asyncio.run(main())