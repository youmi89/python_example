# 1) 라이브러리 설치 : openai
# 2) API KEY 미지정
from openai import OpenAI
client = OpenAI(
    api_key="",
    base_url="https://api.upstage.ai/v1",

    )

completion = client.chat.completions.create(
    model="solar-mini",  # 오픈 에이아이 모
    messages=[
        {
            "role": "user",
            "content": "hello",
        }
    ]
)

print(completion.choices[0].message.content)

# 경로 구분자 : 디렉토리 간 구분자
# 윈도우 : 역슬래시\
# 맥/리눅스 : 슬래시/
