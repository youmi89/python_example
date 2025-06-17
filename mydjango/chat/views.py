# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
# @app.get("/chat") #FastAPI style

    
    # return HttpResponse("hello django")
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html")

# 매 채팅 메세지를 받아 응답 메세지를 만들고 응답하자
# HTTP Methods : GET, POST, PUT/PATCH, DELETE, OPTIONS
# - <form> 태그(유저로부터 입력받아 지정서버로 전송)에서는 GET, POST만 지원
# - GET : 조회목적 -> 요청해도 데이터는 변하지 않는다. -> 검색엔진은 항상 GET요청
# - POST : 파괴적인 액션(추가/수정/삭제 등)
#   - 조회목적인데 POST 요청을 하는 서비스가 있다
#     가급적이면 조회에서는 GET 요청을 쓰시면, 서비스를 최적화 여지가 많고, 
#      이를 도와주는 서비스 / 프로그램도 많다
# - JS API를 통해서 PUT/PATCH, DELETE 등의 요청을 할수 있다
# 링크의 연걸이 된게 HTTP이다 HTTP : 웹페이지, 웹 문서를 위한 프로토콜
def chat_message_new(request: HttpRequest) -> HttpResponse:
    # Query Parameters
    request.GET   # QueryDict 타입 (Dict 으로 보여도 90% 무방)  # POST 요청에서도 있을 수 있어요.
    request.POST  # POST 데이터 (QueryDict)
    
    question = request.POST.get("question", "")
    if question:
        answer = f"당신의 질문 : {question}"
    else:
        answer = "질문이 없으시네요."

    return HttpResponse(answer)
  
# + url encoding = "key=value&key&value=key&value"
# + url encoding 문자열이 요청 주소 뒤에 물음표(?) 뒤에 붙으면 => 그걸 Query Parameters
# + https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python&ackey=4rvenuph

# """
# where=nexearch
# sm=top_hty
# fbm=0
# ie=utf8
# query=python
# ackey=4rvenuph
# """ 
