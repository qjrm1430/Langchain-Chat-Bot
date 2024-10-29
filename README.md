# 기본 랭체인 챗봇

![Langchain Chat Bot](https://img.shields.io/badge/Langchain-ChatBot-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-blue)

## 개요

이 프로젝트는 Langchain과 OpenAI를 활용하여 기본적인 챗봇 구조를 구현한 **기본 랭체인 챗봇**입니다. 사용자는 간단한 설정을 통해 자신의 요구에 맞는 챗봇을 구축하고, Streamlit을 통해 웹 인터페이스로 쉽게 접근할 수 있습니다.

## 주요 기능

- **자연어 처리**: OpenAI의 최신 모델을 활용한 자연스러운 대화
- **확장성**: Langchain을 기반으로 다양한 기능과 모듈을 쉽게 추가 가능
- **웹 인터페이스**: Streamlit을 사용하여 직관적이고 반응형인 웹 UI 제공
- **간편한 설정**: 최소한의 설정으로 빠르게 챗봇을 실행할 수 있는 환경 제공

## 기술 스택

- **Python**: 주 프로그래밍 언어
- **Langchain**: 챗봇의 로직과 흐름을 관리
- **OpenAI**: 자연어 처리 모델 제공
- **Streamlit**: 웹 인터페이스 구축

## 설치 방법

1. **저장소 클론 및 환경 설정**

    ```bash
    git clone https://github.com/qjrm1430/Langchain-Chat-Bot.git
    cd Langchain-Chat-Bot
    python3 -m venv venv
    source venv/bin/activate  # MacOS/Linux
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt
    ```

2. **환경 변수 설정**

    프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 OpenAI API 키를 추가합니다.

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## 사용 방법

1. **챗봇 실행**

    ```bash
    streamlit run app.py
    ```

2. **웹 인터페이스 접근**

    브라우저에서 `http://localhost:8501`로 이동하여 챗봇을 사용합니다.

## 프로젝트 구조

