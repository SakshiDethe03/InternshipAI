import os

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter


load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "google/gemma-4-31b-it:free")


llm = ChatOpenRouter(model=MODEL, api_key=OPENROUTER_API_KEY, temperature=0)
