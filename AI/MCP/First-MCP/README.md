# First-MCP

这是一个基于FastMCP框架的ASCII艺术字生成器示例项目。

## 项目结构

- `server.py`: MCP服务器实现，提供ASCII艺术字生成工具
- `client.py`: MCP客户端示例
- `run_demo.py`: 运行演示的脚本
- `requirements.txt`: 项目依赖文件

## 环境要求

- Python 3.9+
- 虚拟环境（推荐）

## 安装和运行

1. 创建并激活虚拟环境：
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # 或者在Windows上使用: venv\Scripts\activate
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行服务器：
   ```bash
   python3 server.py
   ```

   或运行演示：
   ```bash
   python3 run_demo.py
   ```

## 故障排除

如果遇到 "ModuleNotFoundError: No module named 'fastmcp'" 错误，请确保：
1. 已激活虚拟环境
2. 已安装所有依赖项（`pip install -r requirements.txt`）

# FastMCP ASCII Art Generator Demo

这是一个基于 FastMCP 框架的简单示例，演示如何创建一个 MCP 服务器，该服务器可以根据输入文本生成 ASCII 术字图案。

## 功能

1. 提供两个工具：
   - `generate_ascii_art`: 生成标准的 ASCII 艺术字
   - `generate_simple_ascii_art`: 生成简化的 ASCII 艺术字

2. 支持通过 MCP 协议与 AI 助手集成

## 安装依赖

```bash
pip install -r requirements.txt
```

如果遇到 "externally-managed-environment" 错误，请使用以下命令：
```bash
python3 -m pip install --user --break-system-packages -r requirements.txt
```

推荐使用虚拟环境：
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 运行示例

### 运行服务器

```bash
python3 server.py
```

### 运行客户端测试

```bash
python3 client.py
```

或者使用一体化运行脚本：

```bash
# 运行服务器
python3 run_demo.py

# 运行客户端测试
python3 run_demo.py client
```

## 在Lingma中使用

要将此 MCP 服务器与 Lingma 集成，请按照以下步骤操作：

1. 启动服务器：
   ```bash
   python3 server.py
   ```

2. 在 Lingma 中配置 MCP 连接，指向此服务器

3. 使用自然语言请求生成 ASCII 艺术字，例如：
   - "请为我生成 HELLO 的 ASCII 艺术字"
   - "能帮我把 MCP 转换成字符画吗？"

## 自定义

你可以通过修改 [server.py](server.py) 文件中的 `art_dict` 和 `patterns` 字典来添加更多字符或修改现有字符的图案。