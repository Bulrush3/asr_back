from fastapi import FastAPI

from .api import router


app = FastAPI(
    title='Future ASR Online',
    description='СТРАЙКБОЛ',
    version='1.0.0'
)
app.include_router(router)

