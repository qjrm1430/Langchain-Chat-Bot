from langchain_core.prompts import ChatPromptTemplate

from .constant import CHATBOT_MESSAGE, CHATBOT_ROLE
from .model import create_model


def create_message(prompt):
    # 메시지 딕셔너리 생성
    message = {
        CHATBOT_MESSAGE.role.name: CHATBOT_ROLE.user.name,
        CHATBOT_MESSAGE.content.name: prompt,
    }
    return message


def get_ai_response(messages, callback):
    chat = create_model()
    # 이전 대화 내역을 포함한 프롬프트 생성
    history = []
    for msg in messages:
        role = (
            "assistant"
            if msg[CHATBOT_MESSAGE.role.name] == CHATBOT_ROLE.assistant.name
            else "user"
        )
        history.append((role, msg[CHATBOT_MESSAGE.content.name]))

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "당신은 친절하고 도움이 되는 AI 어시스턴트입니다."),
            *history,
        ]
    )

    # 스트리밍 응답을 위한 체인 생성
    chain = chat_prompt | chat

    # 스트리밍 응답 처리
    response_content = ""
    for chunk in chain.stream({}):
        if chunk.content:
            response_content += chunk.content
            callback(response_content)  # 콜백 함수를 통해 실시간 업데이트

    return {
        CHATBOT_MESSAGE.role.name: CHATBOT_ROLE.assistant.name,
        CHATBOT_MESSAGE.content.name: response_content,
    }
