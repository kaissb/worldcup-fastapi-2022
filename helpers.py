import requests

url = 'https://worldcupjson.net/'


def matches():
    req = requests.get(url + "matches")
    return req


def matches_today():
    req = requests.get(url + "matches/today")
    return req


def matches_current():
    req = requests.get(url + "matches/current")
    return req


def teams():
    req = requests.get(url + "teams")
    return req


def team(code):
    req = requests.get(url + f"teams/{code}")
    return req
