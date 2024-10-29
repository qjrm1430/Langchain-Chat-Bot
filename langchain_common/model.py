from langchain_openai import ChatOpenAI


def create_model():
    # 모델 생성
    chat = ChatOpenAI(model="gpt-4o-mini", streaming=True)
    return chat
