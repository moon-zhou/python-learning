# 问题分析与解决方案

## 问题描述

在运行 `python run_demo.py client` 命令时，出现错误导致程序无法正常执行。

## 问题分析

经过分析，发现以下问题：

1. **命令不存在**：系统中没有 `python` 命令，只有 `python3` 命令
2. **参数类型错误**：在 client.py 中，StdioServerParameters 的 command 参数应该是字符串，但传递的是列表
3. **缺少依赖**：系统中没有安装 fastmcp 依赖包

## 解决方案

### 1. 修复 client.py 中的参数类型错误

将 StdioServerParameters 的参数从：
```python
server_params = StdioServerParameters(
    command=["python3", "server.py"],
    cwd="."
)
```

修改为：
```python
server_params = StdioServerParameters(
    command="python3",
    args=["server.py"],
    cwd="."
)
```

### 2. 安装项目依赖

使用以下命令安装项目依赖：
```bash
python3 -m pip install --user --break-system-packages "fastmcp>=2.12.2"
```

## 验证结果

修复后，运行以下命令可以正常工作：
```bash
python3 run_demo.py client
```

程序能够：
1. 成功启动 MCP 服务器
2. 列出可用工具
3. 正确调用工具生成 ASCII 艺术字

## 建议改进

1. 在 README.md 中明确说明使用 `python3` 而不是 `python` 命令
2. 考虑使用虚拟环境管理项目依赖
3. 更新文档，添加依赖安装说明