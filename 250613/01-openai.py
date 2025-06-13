# 1) 라이브러리 설치 : openai
# 2) API KEY 미지정
from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
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
