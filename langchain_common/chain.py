# 체인 생성 = 프롬프트 + 모델
def create_chain(chat, chat_prompt):
    chain = chat_prompt | chat
    return chain
