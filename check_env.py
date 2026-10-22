import os

from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")
sec_user_agent = os.getenv("SEC_USER_AGENT")

if api_key is None:
    raise RuntimeError("API_KEY is missing from .env")

if sec_user_agent is None:
    raise RuntimeError("SEC_USER_AGENT is missing from .env")

print(f"{api_key[:4]}...")
print(sec_user_agent)
