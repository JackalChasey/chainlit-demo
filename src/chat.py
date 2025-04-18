"""
聊天模块: 处理聊天会话和消息流
"""
import chainlit as cl
from typing import Dict, List, Any, Optional

from src.models import get_streaming_response
from src.config import DEFAULT_MODEL, DEFAULT_TEMPERATURE

# 使用缓存存储聊天历史
@cl.cache
def get_messages():
    """获取聊天历史记录"""
    return []

async def process_user_message(message: cl.Message) -> None:
    """
    处理用户消息并生成流式响应
    
    Args:
        message: 用户消息对象
    """
    # 获取当前聊天历史和设置
    messages = get_messages()
    model = cl.user_session.get("model", DEFAULT_MODEL)
    temperature = cl.user_session.get("temperature", DEFAULT_TEMPERATURE)
    
    # 将用户消息添加到聊天历史
    messages.append({"role": "user", "content": message.content})
    
    response_message = cl.Message(content="")
    await response_message.send()
    
    # 获取流式响应
    stream = await get_streaming_response(
        messages=messages,
        model=model,
        temperature=temperature
    )
    
    # 初始化内容缓冲区
    content_buffer = ""
    thinking_buffer = "<thinking>"
    
    # 处理流式响应
    async for chunk in stream:
        # 处理思考过程（如果有的话）
        if hasattr(chunk.choices[0].delta, 'reasoning_content'):
            thinking_piece = chunk.choices[0].delta.reasoning_content
            thinking_buffer += thinking_piece
            response_message.content = thinking_buffer
            await response_message.update()

        # 处理正常的内容输出
        if hasattr(chunk.choices[0].delta, 'content'):
            content_piece = chunk.choices[0].delta.content
            content_buffer += content_piece
            
            # 更新消息内容以实现流式效果
            response_message.content = thinking_buffer + "<thinking>" + content_buffer
            await response_message.update()     
    
    # 将助手的完整响应添加到聊天历史
    messages.append({"role": "assistant", "content": content_buffer})

async def init_chat_session():
    """初始化新的聊天会话"""
    # 发送欢迎消息
    await cl.Message(content="你好！我是一个类似ChatGPT的AI助手。我能帮你什么忙吗？").send()
    
    # 初始化聊天历史
    get_messages().clear()
    
    # 设置会话参数
    cl.user_session.set("model", DEFAULT_MODEL)
    cl.user_session.set("temperature", DEFAULT_TEMPERATURE)
