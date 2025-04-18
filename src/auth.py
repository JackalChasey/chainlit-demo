"""
认证模块: 处理用户认证
"""
import chainlit as cl
from typing import Optional

from src.config import AUTH_USERS

def authenticate_user(username: str, password: str) -> Optional[cl.User]:
    """
    验证用户身份
    
    Args:
        username: 用户名
        password: 密码
        
    Returns:
        如果验证成功，返回User对象；否则返回None
    """
    if username in AUTH_USERS and AUTH_USERS[username]["password"] == password:
        return cl.User(
            identifier=username,
            metadata={"role": AUTH_USERS[username]["role"], "provider": "credentials"}
        )
    return None 