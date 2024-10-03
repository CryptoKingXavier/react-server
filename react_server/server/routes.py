from os import system
from typing import Literal
from flask import Blueprint
from http import HTTPStatus
from threading import Thread, ThreadError

server: Blueprint = Blueprint("server", __name__)

def json_server() -> int:
    system("json-server ./react_server/jobs.json")

@server.get("/")
def index() -> tuple[str, Literal[200]]:
    try:
        thread: Thread = Thread(target=json_server)
        thread.start()
    except ThreadError:
        print("JSON Server Suddenly Stopped!")
    return "JSON Server Started Successfully!", HTTPStatus.OK.value
