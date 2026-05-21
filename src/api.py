from fastapi import FastAPI
from .core import build_greeting

app = FastAPI(title="Greetings API")

@app.get("/greet")
def greet_endpoint(
    name: str = "",
    title: str = "",
    doctor: bool = False,
    count: int = 1,
):
    message = build_greeting(name, title, doctor, count)
    return {"message": message}