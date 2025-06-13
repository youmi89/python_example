from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://api.upstage.ai/v1",
)

# stream 여부에 따라 변환값이 다르다
stream = client.chat.completions.create(
    model="solar-pro2-preview",
    messages=[
        {
            "role": "user",
            "content": "오늘 비가 오는데 뭘 먹으면 좋을까?",
        }
    ],
    stream=True, 
)
# stream=False : 통응답을 받을 때
# print(completion.choices)

# API 서버에서 내려준 chunk 개수만큼 반복된다
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        # end 키워드 인자의 디폴드 값 : 개행 ("\n")
        print(chunk.choices[0].delta.content, end="")
