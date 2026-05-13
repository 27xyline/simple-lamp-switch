from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
INDEX_HTML = BASE_DIR / "index.html"

lamp_is_on = False


@app.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    return HTMLResponse(INDEX_HTML.read_text(encoding="utf-8"))


@app.get("/status")
def get_status() -> dict[str, bool]:
    return {"is_on": lamp_is_on}


@app.post("/toggle")
def toggle_lamp() -> dict[str, bool]:
    global lamp_is_on
    lamp_is_on = not lamp_is_on
    return {"is_on": lamp_is_on}


@app.get("/toggle")
def toggle_lamp_from_url() -> dict[str, bool]:
    return toggle_lamp()
