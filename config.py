from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")

MODEL_NAME = "deepseek-ai/DeepSeek-V3.2"
BASE_URL = "https://api.siliconflow.cn/v1"

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)