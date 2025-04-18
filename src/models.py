"""
模型模块: 处理与OpenAI API的所有交互
"""
from openai import AsyncOpenAI
from typing import List, Dict, Any

from src.config import OPENAI_API_KEY, BASE_URL, DEFAULT_MODEL, DEFAULT_TEMPERATURE

# 初始化OpenAI异步客户端
client = AsyncOpenAI(api_key=OPENAI_API_KEY, base_url=BASE_URL)

async def get_streaming_response(messages: List[Dict[str, str]], 
                                model: str = DEFAULT_MODEL, 
                                temperature: float = DEFAULT_TEMPERATURE):
    """
    获取OpenAI的流式响应
    
    Args:
        messages: 对话历史消息列表
        model: 使用的OpenAI模型
        temperature: 温度参数，控制响应的随机性
        
    Returns:
        生成器，产生来自OpenAI API的流式响应
    """
    stream = await client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        temperature=temperature,
        timeout=1800
    )
    return stream
    
async def analyze_file_content(file_content: str, file_name: str, 
                              model: str = DEFAULT_MODEL,
                              temperature: float = DEFAULT_TEMPERATURE) -> str:
    """
    分析文件内容
    
    Args:
        file_content: 文件内容
        file_name: 文件名
        model: 使用的OpenAI模型
        temperature: 温度参数，控制响应的随机性
        
    Returns:
        分析结果字符串
    """
    messages = [
        {"role": "system", "content": "你是一个专门分析文件内容的助手。"},
        {"role": "user", "content": f"分析以下来自文件{file_name}的内容:\n\n{file_content}"}
    ]
    
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    return response.choices[0].message.content 