from pathlib import Path

from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
INDEX_HTML = BASE_DIR / "index.html"

hand_is_closed = False

def hand_status() -> dict[str, bool | str]:
    return {
        "is_closed": hand_is_closed,
        "state": "closed" if hand_is_closed else "open",
    }


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def index() -> HTMLResponse:
    return HTMLResponse(INDEX_HTML.read_text(encoding="utf-8"))


@app.get("/status", status_code=status.HTTP_200_OK)
def get_status() -> dict[str, bool | str]:
    return hand_status()


@app.api_route("/open", methods=["GET", "POST"], status_code=status.HTTP_200_OK)
def open_hand() -> dict[str, bool | str]:
    global hand_is_closed
    hand_is_closed = False
    return hand_status()


@app.api_route("/close", methods=["GET", "POST"], status_code=status.HTTP_200_OK)
def close_hand() -> dict[str, bool | str]:
    global hand_is_closed
    hand_is_closed = True
    return hand_status()
