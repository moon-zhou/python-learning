# 在 Lingma 中配置 FastMCP ASCII Art Generator

本文档介绍了如何在 Lingma 中配置和使用 FastMCP ASCII Art Generator。

## 启动 MCP 服务器

首先，您需要启动 ASCII Art Generator 服务器：

```bash
python3 server.py
```

默认情况下，服务器将使用 stdio（标准输入输出）方式进行通信。

## 在 Lingma 中配置 MCP 连接

### 1. 打开 Lingma 的 MCP 配置界面

在 Lingma 应用中找到 MCP 或插件配置选项。

### 2. 添加新的 MCP 连接

点击"添加 MCP 服务器"或类似选项。

### 3. 配置连接参数

配置以下参数：

- **名称**: ASCII Art Generator
- **类型**: stdio（标准输入输出）
- **命令**: `python3`
- **参数**: `server.py`
- **工作目录**: 项目的绝对路径，例如：`~/working/selfcodespace/python-learning/AI/MCP/First-MCP`

示例配置：
```
名称: ASCII Art Generator
类型: stdio
命令: python3
参数: server.py
工作目录: ~/working/selfcodespace/python-learning/AI/MCP/First-MCP
```

### 4. 保存并连接

保存配置并尝试连接到服务器。

## 使用工具

连接成功后，您可以使用自然语言请求生成 ASCII 艺术字，例如：

- "请为我生成 HELLO 的 ASCII 艺术字"
- "能帮我把 MCP 转换成字符画吗？"
- "使用简化样式为我的名字 LINGMA 创建 ASCII 艺术字"

## 可用工具

服务器提供两个工具：

1. **generate_ascii_art**
   - 功能：生成标准的 ASCII 艺术字
   - 参数：text（需要转换为 ASCII 艺术字的文本）

2. **generate_simple_ascii_art**
   - 功能：生成简化的 ASCII 艺术字
   - 参数：text（需要转换为 ASCII 艺术字的文本）

## 故障排除

如果遇到问题，请检查：

1. 确保已安装所有依赖项：
   ```bash
   python3 -m pip install --user --break-system-packages -r requirements.txt
   ```

2. 确保使用的是 `python3` 而不是 `python` 命令

3. 确保工作目录设置正确

4. 查看 [ISSUE_RESOLUTION.md](file://~/working/selfcodespace/python-learning/AI/MCP/First-MCP/ISSUE_RESOLUTION.md) 文件了解常见问题及解决方案