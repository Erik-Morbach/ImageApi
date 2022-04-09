from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import controller.controller

app = FastAPI()


@app.get("/")
async def root():
    content = "<p> Hello World"
    return HTMLResponse(content=content)

app.include_router(controller.controller.router)
