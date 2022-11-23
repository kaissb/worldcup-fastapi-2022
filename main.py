from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from helpers import matches, matches_today, matches_current, teams, team

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/')
async def index(request: Request):
    context = {
        "request": request,
        "_matches": matches().json(),
        "_matches_current": matches_current().json(),
        "_matches_today": matches_today().json(),
        "_teams": teams().json(),
    }
    return templates.TemplateResponse("index.html", context)
