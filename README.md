# 流式响应ChatGPT模拟器

基于Chainlit和OpenAI API构建的具有流式响应的聊天机器人应用，提供类似ChatGPT的用户体验。

## 功能特点

- OpenAI响应的实时流式输出（类似ChatGPT）
- 会话内持久化的聊天历史
- 文件上传与内容分析功能
- 聊天建议（提示语）选项
- 简单的身份验证系统
- 优雅地处理停止请求

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
    └── models.py          # OpenAI API交互模块
```

## 安装步骤

1. 克隆仓库并进入项目目录

2. 安装所需的依赖项：
   ```
   pip install -r requirements.txt
   ```

3. 创建一个包含OpenAI API密钥的`.env`文件：
   ```
   cp .env.example .env
   ```
   然后编辑`.env`文件，填入您的实际OpenAI API密钥。

4. 运行应用程序：
   ```
   chainlit run app.py -w
   ```

5. 在浏览器中打开以下地址：
   ```
   http://localhost:8000
   ```

## 身份验证

应用程序包含一个简单的用户名/密码认证系统：
- 管理员访问：用户名`admin`，密码`admin`
- 用户访问：用户名`user`，密码`pass`

您可以通过编辑`src/config.py`文件中的`AUTH_USERS`字典来修改这些凭据。

## 自定义选项

- 在`src/config.py`中更改默认的OpenAI模型和温度参数
- 在`src/chat.py`中自定义聊天启动器（提示语）
- 修改`chainlit.yaml`调整UI外观和行为

## 如何扩展

1. 添加新的对话功能：扩展`src/chat.py`模块
2. 支持更多文件类型：在`src/file_handler.py`中添加处理逻辑
3. 实现更复杂的认证：修改`src/auth.py`模块

## 注意事项

- 聊天历史仅在会话期间保持
- 在生产环境中，请实施更安全的认证机制
- OpenAI API调用会产生费用，请注意您的使用量
