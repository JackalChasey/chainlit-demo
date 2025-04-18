"""
配置模块: 处理环境变量和应用程序配置
"""
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# OpenAI API配置: 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")

# 默认模型参数
DEFAULT_MODEL = "ep-20250205160314-8vx9f" # doubao-1-5-thinking-pro-250415
DEFAULT_TEMPERATURE = 0.7

# 认证配置
AUTH_USERS = {
    "admin": {"password": "admin", "role": "ADMIN"},
    "user": {"password": "pass", "role": "USER"}
} 
