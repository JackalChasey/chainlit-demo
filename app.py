"""
主应用模块: 注册Chainlit钩子并初始化应用
"""
import chainlit as cl
from typing import Dict, List, Any

from src.chat import process_user_message, init_chat_session
from src.auth import authenticate_user
from src.file_handler import process_uploaded_file

@cl.on_chat_start
async def on_chat_start():
    """聊天开始时执行的操作"""
    await init_chat_session()

@cl.on_message
async def on_message(message: cl.Message):
    """接收到用户消息时执行的操作"""
    await process_user_message(message)

# @cl.on_file_upload(accept=["text/plain", "application/pdf", "application/json", "text/markdown"])
# async def on_file_upload(file: cl.File):
#     """接收到文件上传时执行的操作"""
#     await process_uploaded_file(file)

@cl.on_stop
async def on_stop():
    """执行停止请求时的操作"""
    return "我已停止生成响应。"

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    """身份验证回调"""
    return authenticate_user(username, password)

if __name__ == "__main__":
    # 此代码块仅在直接运行app.py时执行，而不是通过chainlit run app.py执行
    print("请使用 'chainlit run app.py' 命令启动应用！") 