# Chainlit 多模态聊天机器人学习项目

这是一个基于 Chainlit 构建的聊天机器人学习项目，旨在探索和实践如何创建一个功能丰富的 AI 聊天应用。项目重点是学习如何集成各大 AI 平台的 API，以及如何处理多种媒体类型的输入和输出。

## 项目目标

- 学习如何调用各大 AI 平台的 API（OpenAI, Anthropic, Google AI 等）
- 实现在对话中处理图片、文件等多模态内容的能力
- 探索让 AI 生成和输出各种媒体类型（图片、文件、语音等）的方法
- 了解和应用流式响应技术，提供更自然的对话体验

## 当前功能

- ✅ 基于 OpenAI API 的流式文本响应
- ✅ 会话内持久化的聊天历史
- ✅ 简单的身份验证系统
- ✅ 优雅地处理停止请求

## 待实现功能 (TODO)

- 🔄 文件上传与内容分析（已部分实现）
- 📊 多种文件格式的处理（PDF, CSV, JSON 等）
- 🖼️ 图像处理和分析能力
- 🔊 语音转文本及文本转语音功能
- 🌐 多 AI 模型切换和对比
- 📝 聊天记录导出功能
- 🔗 API 密钥管理系统
- 📱 响应式 UI 优化

## 项目结构

```
.
├── app.py                 # 主程序入口点
├── chainlit.md            # Chainlit欢迎页面配置
├── chainlit.yaml          # Chainlit应用配置
├── requirements.txt       # 项目依赖
├── .env.example           # 环境变量示例
└── src/                   # 源代码目录
    ├── __init__.py        # 包初始化文件
    ├── auth.py            # 认证模块
    ├── chat.py            # 聊天处理模块
    ├── config.py          # 配置模块
    ├── file_handler.py    # 文件处理模块
    └── models.py          # AI 模型 API 交互模块
```

## 安装步骤

1. 克隆仓库并进入项目目录

2. 安装所需的依赖项：
   ```
   pip install -r requirements.txt
   ```

3. 创建一个包含 API 密钥的 `.env` 文件：
   ```
   cp .env.example .env
   ```
   然后编辑 `.env` 文件，填入您的实际 API 密钥。

4. 运行应用程序：
   ```
   chainlit run app.py -w
   ```

5. 在浏览器中打开以下地址：
   ```·
   http://localhost:8000
   ```

## 身份验证

应用程序包含一个简单的用户名/密码认证系统：
- 管理员访问：用户名 `admin`，密码 `admin`
- 用户访问：用户名 `user`，密码 `pass`

## 学习路径与资源

本项目作为学习 AI 应用开发的工具，涵盖以下学习领域：
- Chainlit 框架基础与高级功能
- API 集成与管理
- 多模态内容处理
- 流式响应技术

## 许可证

[MIT](LICENSE)

## 鸣谢

- [Chainlit](https://github.com/Chainlit/chainlit) - 提供构建 AI 聊天应用的强大框架
- 各大 AI 服务提供商（OpenAI, Anthropic, Google AI 等）
