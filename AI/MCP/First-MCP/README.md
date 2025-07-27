# MCP (Model Context Protocol) Python 示例

这个项目演示了如何使用Python实现一个简单的MCP（Model Context Protocol）服务器和客户端。

## 什么是MCP？

MCP（Model Context Protocol）是由Anthropic提出的一种开放协议，允许AI模型安全地访问外部工具、资源和上下文信息。它定义了客户端（如AI助手）和服务器（提供工具和资源）之间的通信标准。

## 项目结构

- [mcp_server.py](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/mcp_server.py) - 简单的MCP服务器实现
- [mcp_client.py](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/mcp_client.py) - 简单的MCP客户端实现
- [requirements.txt](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/requirements.txt) - 项目依赖
- [run_demo.py](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/run_demo.py) - 演示运行脚本

## 运行示例

### 方法1：使用虚拟环境（推荐）

1. 创建虚拟环境：
```bash
python3 -m venv mcp_env
```

2. 激活虚拟环境：
```bash
# macOS/Linux
source mcp_env/bin/activate

# Windows
mcp_env\Scripts\activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 启动服务器：
```bash
python mcp_server.py
```

5. 在另一个终端中运行客户端（确保虚拟环境已激活）：
```bash
python mcp_client.py
```

### 方法2：直接运行

如果系统允许直接安装包，可以运行演示脚本：

```bash
python run_demo.py
```

## 常见问题

### ModuleNotFoundError: No module named 'websockets'

如果遇到此错误，表示缺少 [websockets](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/venv/bin/websockets) 依赖。请确保已安装所有依赖项：

```bash
pip install -r requirements.txt
```

在某些系统（如较新的Ubuntu、Debian或macOS）上，可能需要使用虚拟环境或添加 `--user` 标志：

```bash
# 使用虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 或者使用 --user 标志
pip install --user -r requirements.txt
```

## 功能演示

本示例演示了MCP的核心功能：
1. 服务器初始化
2. 工具列表获取
3. 工具调用（计算器和天气查询）
4. 资源访问

## 代码说明

### 服务器端 ([mcp_server.py](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/mcp_server.py))

服务器实现了以下MCP功能：
- WebSocket连接处理
- 工具注册（计算器和天气查询）
- 资源提供（README和用户数据）
- 消息处理和响应

### 客户端 ([mcp_client.py](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/mcp_client.py))

客户端实现了以下功能：
- 与服务器建立WebSocket连接
- 发送MCP请求消息
- 接收和处理服务器响应
- 调用各种工具和资源

## 扩展建议

要基于此示例构建更完整的MCP应用，可以考虑：

1. 使用官方的MCP Python SDK：
```bash
pip install mcp
```

2. 添加更多实用工具，如文件操作、网络请求等
3. 实现更复杂的资源管理功能
4. 添加认证和权限控制
5. 实现持久化存储

# AI/MCP 目录说明

这个目录包含了与MCP (Model Context Protocol) 相关的示例和项目。

## 目录结构

- [First-MCP](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP) - 第一个MCP示例项目，包含完整的MCP服务器和客户端实现

## First-MCP 示例

[First-MCP](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP) 目录中包含了一个完整的MCP示例，演示了如何使用Python实现MCP服务器和客户端。

### 功能特性

1. 基于WebSocket的MCP服务器实现
2. MCP客户端实现
3. 工具注册和调用（计算器和天气查询）
4. 资源提供和访问
5. 完整的MCP协议消息处理

### 如何运行

请查看 [First-MCP/README.md](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/README.md) 获取详细的运行说明。
