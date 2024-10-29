# 랭체인 기본 챗봇

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Langchain](https://img.shields.io/badge/Langchain-00C7B7?logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-343541?logo=openai&logoColor=white)

## 개요

Langchain과 OpenAI를 활용하여 기본적인 챗봇 구조를 구현한 프로젝트입니다. 사용자는 간단한 설정을 통해 자신의 요구에 맞는 챗봇을 구축하고, Streamlit을 통해 웹 인터페이스로 쉽게 접근할 수 있습니다.

## 목차

- [개요](#개요)
- [기술 스택](#기술-스택)
- [설치 방법](#설치-방법)
- [사용 방법](#사용-방법)
- [환경 변수 설정](#환경-변수-설정)
- [기여](#기여)
- [라이선스](#라이선스)
- [문의](#문의)

## 기술 스택

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Langchain](https://img.shields.io/badge/Langchain-00C7B7?logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-343541?logo=openai&logoColor=white)

## 설치 방법

1. **저장소 클론하기**

    ```bash
    git clone https://github.com/qjrm1430/Langchain-Chat-Bot.git
    cd Langchain-Chat-Bot
    ```

2. **가상 환경 생성 및 활성화**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. **필요한 패키지 설치**

    ```bash
    pip install -r requirements.txt
    ```

## 사용 방법

1. **환경 변수 설정**

    프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음과 같이 설정합니다:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

2. **애플리케이션 실행**

    ```bash
    streamlit run app.py
    ```

3. **웹 인터페이스 접근**

    브라우저에서 `http://localhost:8501`으로 접속하여 챗봇을 사용합니다.

## 환경 변수 설정

프로젝트를 실행하기 위해서는 OpenAI API 키가 필요합니다. `.env` 파일을 생성하고 다음과 같이 설정하세요:

```env
OPENAI_API_KEY=your_openai_api_key
