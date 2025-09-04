#!/usr/bin/env python3

import subprocess
import sys
import os

def run_server():
    """运行MCP服务器"""
    print("Starting MCP Server...")
    try:
        # 切换到当前目录
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # 启动服务器
        server_process = subprocess.Popen(
            ["python3", "server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("MCP Server started successfully!")
        print("Server PID:", server_process.pid)
        return server_process
    except Exception as e:
        print(f"Failed to start server: {e}")
        return None

def run_client():
    """运行客户端示例"""
    print("Running client demo...")
    try:
        # 切换到当前目录
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # 运行客户端
        result = subprocess.run(
            ["python3", "client.py"],
            capture_output=True,
            text=True
        )
        
        print("Client output:")
        print(result.stdout)
        if result.stderr:
            print("Client errors:")
            print(result.stderr)
            
        return result.returncode == 0
    except Exception as e:
        print(f"Failed to run client: {e}")
        return False

def main():
    print("FastMCP ASCII Art Demo")
    print("=" * 30)
    
    if len(sys.argv) > 1 and sys.argv[1] == "client":
        # 运行客户端
        run_client()
    else:
        # 默认运行服务器
        server_process = run_server()
        if server_process:
            try:
                # 等待用户中断
                server_process.wait()
            except KeyboardInterrupt:
                print("\nShutting down server...")
                server_process.terminate()
                server_process.wait()
                print("Server stopped.")

if __name__ == "__main__":
    main()