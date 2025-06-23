# Create your views here.
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from chat.models import PuzzleRoom
from chat.forms import PuzzleRoomForm, PuzzleRoomEditForm

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
    request.GET  # QueryDict 타입 (Dict 으로 보여도 90% 무방)  # POST 요청에서도 있을 수 있어요.
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

# TODO: 왜 puzzle_room_list가 아니라 puzzleroom_list 인가요?


def puzzleroom_list(request):
    # puzzle room 테이블에 있는 모든 레코드를 가져올 준비
    qs = PuzzleRoom.objects.all()  # QuerySet 타입
    return render(
        request,
        template_name="chat/puzzleroom_list.html",
        context={"puzzleroom_list": qs},
    )


# chat/views.py

# # chat/urls.py 에서 name 인자를 추출해서
# View 함수 호출 시에 자동으로 인자를 전달해줍니다.


def puzzleroom_play(request: HttpRequest, id: int) -> HttpResponse:

    # id 값을 통해서, 아래 값을 찾아서 할당을 할 겁니다.

    room = PuzzleRoom.objects.get(id=id)
    image_url = room.image_file.url
    level = room.level

    # toy, mario, flower, game
    # # 외부로부터 전달받은 값은 절대 신뢰해서는 안 됩니다.
    # # 우리가 원하는 규칙에 맞는 지, 항상 검사해야만 합니다. (중요 ** 10000000)

    # # 없는 데이터를 요청했는 데, 500 서버 에러로 기록되는 것은 서버 개발자는 억울합니다.
    # # 없는 데이터는 404 Page not found 응답을 하는 것이 맞습니다.
    # #TODO: image_url/level 설정을 View 단에 하드 코딩이 아니라
    # #유저가 이미지와 레벨을 설정해서 게임방을 만들수 있으면 좋겠다
    # # => 이러한 보통은 데이터베이스에 저장/수정하고 불러서 활용한다
    # # 보통의 애플리케이션들은 대개 데이터베이스 중심의 소프트웨어다

    # try:
    #     image_url = {
    #     "mario": "/static/chat/mario.jpg",
    #     "toy": "/static/chat/toy-story.jpg",
    #     "openai-1": "/static/chat/openai-1.png",
    # }[name]
    # except KeyError:
    #     # 위에서 임포트 : from django.http import Http404
    #     raise Http404(f"not found room : {name}")
    #     # return Http404  # return 쓰시면 안 되요 !!
    # level = 3

    # toy, mario, flower, game
    return render(
        request,
        # 이 템플릿 내의 코드는 모두 그냥 문자열 !!!
        template_name="chat/puzzle.html",
        # "image_url" 이라는 이름으로 image_url 값을 전달합니다.
        # 대개 같은 이름으로 지정합니다.
        context={
            "image_url": image_url,
            "level": level,
        },
    )


# 1개의 PuzzleRoom 생성하기 위해서, 최소 2번의 요청을 받을 것이다
# 1. GET 요청 :빈 입력 서식을 보여줘야 한다
# 2. POST 요청 :유저가 서식에 값을 채우고, 전송(저장) 버튼을 눌렀을 떄 유저의 입력값을 전송(반복)
def puzzleroom_new(request: HttpRequest) -> HttpResponse:
    form = PuzzleRoomForm()

    if request.method == "GET":  # "GET" or "POST" 뿐. (항상 대문자)
        form = PuzzleRoomForm()

    else:  # "POST" : 유저가 입력한 값에 대한 유효성 검사, pass(저장), fail(에러 응답)
        # request.POST   # POST 요청에서의 데이터 (파일 제외)
        # request.FILES  # POST 요청에서의 데이터 (파일 만)

        # Form에게 유저의 모든 입력 데이터를 전달
        form = PuzzleRoomForm(data=request.POST, files=request.FILES)
        # form : 유저가 전달한 값을 모두 알고 있습니다. + 입력 필드 구성도 모두 알고 있습니다.

        # 호출 즉시, 유효성 검사를 수행합니다.
        # 단 1개의 유효성 검사라도 실패하면, False 반환. 모두 통과하면 True 반환
    if form.is_valid():
        form.save()  # 데이터베이스에 저장합니다. (ModleForm 만의 기능)
        # TODO: 성공 메시지, 저장된 게임룸으로 즉시 이동
        return redirect("/chat/puzzle/")  # django.shortcuts
    else:
        pass  # 아래 템플릿 렌더링을 합니다. +에러 출력 기능까지 있다

    # 장고의 문화 대로, 파일명과 View 이름을 쓰고 있다
    return render(
        request,
        template_name="chat/puzzleroom_form.html",
        context={
            "form": form,
        },
    )


def puzzleroom_edit(request: HttpRequest, id: int) -> HttpResponse:
    # 수정 대상을 데이터베이스에서 조회
    room = PuzzleRoom.objects.get(id=id)

    if request.method == "GET":
        form = PuzzleRoomEditForm(instance=room)

    else:
        form = PuzzleRoomEditForm(instance=room, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/chat/puzzle/")

    return render(
        request,
        # 이 템플릿 내의 코드는 모두 문자열!
        "chat/puzzleroom_form.html",
        # "image_url" 이라는 이름으로 image_url 값을 전달한다
        # 대개 같은 이름으로 지정한다
        {
            "form": form,
        },
    )
