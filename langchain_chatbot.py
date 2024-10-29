from dotenv import load_dotenv

# .env 파일에 등록된 변수(데이터)를 os 환경변수에 적용
load_dotenv()

from langchain_common.constant import CHATBOT_ROLE, CHATBOT_MESSAGE
from langchain_common.prompt import create_message, get_ai_response

# web ui/ux
import streamlit as st

st.title("Chat Bot")

# 메세지를 저장
# messages = {"role":"", "content":""}
#   role -> user(사용자) / assistant(AI)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 저장한 메세지를 화면에 표현
for message in st.session_state.messages:
    with st.chat_message(message[CHATBOT_MESSAGE.role.name]):
        st.markdown(message[CHATBOT_MESSAGE.content.name])

# 사용자 입력
prompt = st.chat_input("입력해주세요")
if prompt:
    # 사용자 메시지 생성 및 저장
    user_message = create_message(prompt=prompt)
    st.session_state.messages.append(user_message)

    # 사용자 메시지 표시
    with st.chat_message(CHATBOT_ROLE.user.name):
        st.markdown(prompt)

    # AI 응답을 위한 컨테이너 생성
    with st.chat_message(CHATBOT_ROLE.assistant.name):
        response_placeholder = st.empty()

        # 스트리밍 콜백 함수
        def update_response(content):
            response_placeholder.markdown(content)

        # AI 응답 생성 및 저장
        ai_message = get_ai_response(st.session_state.messages, update_response)
        st.session_state.messages.append(ai_message)
