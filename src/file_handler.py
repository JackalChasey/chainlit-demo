"""
文件处理模块: 处理文件上传和分析
"""
import chainlit as cl
from typing import Dict, List, Any

from src.models import analyze_file_content

async def process_uploaded_file(file: cl.File) -> None:
    """
    处理上传的文件
    
    Args:
        file: 上传的文件对象
    """
    # 开始一个文件处理步骤
    async with cl.Step(name=f"正在处理文件: {file.name}") as step:
        # 读取文件内容
        if file.type.startswith("text/") or file.type == "application/json" or file.type == "application/pdf":
            file_content = file.content.decode("utf-8")
            
            # 限制显示内容长度
            preview = file_content[:500] + "..." if len(file_content) > 500 else file_content
            
            # 为文件内容创建文本元素
            text_element = cl.Text(
                name=file.name,
                content=preview,
                display="side",  # 在侧面板中显示
                language=file.name.split(".")[-1] if "." in file.name else "text"
            )
            
            # 处理文件内容
            model = cl.user_session.get("model")
            temperature = cl.user_session.get("temperature")
            analysis = await analyze_file_content(
                file_content=file_content, 
                file_name=file.name,
                model=model,
                temperature=temperature
            )
            
            # 发送带有文本元素的响应
            await cl.Message(
                content=f"### {file.name}分析结果\n\n{analysis}",
                elements=[text_element]
            ).send()
            
            # 更新步骤状态为成功
            step.output = f"成功处理{file.name}"
        else:
            step.output = f"不支持的文件类型: {file.type}"
            await cl.Message(content=f"抱歉，我无法处理{file.type}类型的文件。").send() 