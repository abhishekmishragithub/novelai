from langchain_openai import ChatOpenAI

def create_chat_openai_instance(tuneai_api_key):
    return ChatOpenAI(
        api_key=tuneai_api_key,
        base_url="https://proxy.tune.app/",
        model="openai/gpt-4o",
    )
