
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# @app.get("/")
# def read_root():
#     return{"이름": 2 * 22, "age": 20}

# @app.post("/")
# def post_root():
#     return {"이건": "포스트입니다."}

# @app.get("/good")
# def read_goo():
#     return {"a": 1}

# @app.get("/todo")
# def read_root():
#     return{"이름": ""}

# @app.get("/")
# def read_root():
#     return {"이름": 2 * 22, "age": 20}


notices = ["공지사항1", "공지사항2", "공지사항3"]


@app.get("/")  # -> 127.0.0.1:8000 get method
def read_root():
    return {"Hello": "World!"}


@app.get("/about") # -> 127.0.0.1:8000/about get method
def about():
    return {"message": "about page"}


@app.get("/contact") # -> 127.0.0.1:8000/contact get method
def contact():
    return {"message": "contact page"}


@app.get("/notice") # -> 127.0.0.1:8000/notice get method
def notice():
    return {"notice": notices}

@app.get("/index", response_class=HTMLResponse)
def index():
    return "<h1> 날씨가 너무 덥다 </h1>"

templates = Jinja2Templates(directory="templates")  # templates 폴더를 지정합니다.

@app.get("/index2") # -> 127.0.0.1:8000/index2 get method
def index2(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

