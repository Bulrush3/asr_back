from fastapi import FastAPI
from starlette.responses import HTMLResponse

from .api import router


app = FastAPI(
    title='Future ASR Online',
    description='СТРАЙКБОЛ РУЛИТ',
    version='1.0.0'
)
app.include_router(router)

@app.get("/sosi")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)
