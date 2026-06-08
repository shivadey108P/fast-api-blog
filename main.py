from fastapi import FastAPI, Request

# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")


posts: list[dict] = [
    {
        "id": 1,
        "author": "Shiva Dey",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy to learn and use. I highly recommend it to everyone",
        "date_posted": "April 20, 2026",
    },
    {
        "id": 2,
        "author": "John Doe",
        "title": "Python is the best programming language",
        "content": "I have been using Python for years and I can say that it is the best programming language out there. It is easy to learn, versatile and has a huge community.",
        "date_posted": "April 21, 2026",
    },
]


@app.get("/", include_in_schema=False, name='home')
@app.get("/posts", include_in_schema=False, name='posts')
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={"posts": posts, "title": "Home"}
    )


@app.get("/api/posts")
def get_posts():
    return posts


if __name__ == "__main__":
    pass
