from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from helpers import matches, matches_today, matches_current, teams, team

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def test(request: Request):

    context = {
        "request": request,
        "_matches": matches().json(),
        "_matches_current": matches_current().json(),
        "_matches_today": matches_today().json(),
        "_teams": teams().json(),
    }
    return templates.TemplateResponse("test.html", context)


@app.get("/")
async def index(request: Request):
    context = {
        "request": request,
        "_matches": matches().json(),
        "_matches_current": matches_current().json(),
        "_matches_today": matches_today().json(),
        "_teams": teams().json(),
    }
    return templates.TemplateResponse("index.html", context)


@app.get("/team/{code}")
async def team_view(request: Request, code: str):
    team_data = team(code).json()

    context = {
        "request": request,
        "_team_data": team_data,
        "_name": team_data.get("name"),
        "_wins": team_data.get("wins"),
        "_draws": team_data.get("draws"),
        "_losses": team_data.get("losses"),
        "_games_played": team_data.get("games_played"),
        "_group_points": team_data.get("group_points"),
        "_goals_for": team_data.get("goals_for"),
        "_goals_against": team_data.get("goals_against"),
        "_goal_differential": team_data.get("goal_differential"),
    }
    return templates.TemplateResponse("team.html", context)
