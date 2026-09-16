import os

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter


load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenRouter(
    model="google/gemini-2.5-flash-lite",
    api_key=OPENROUTER_API_KEY,
    temperature=0,
    max_tokens=2048,
)
