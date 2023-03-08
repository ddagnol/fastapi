from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router,prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True, log_level='info')


'''
{
    "acess_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc4ODg4MzcwLCJpYXQiOjE2NzgyODM1NzAsInN1YiI6IjcifQ.HA2_2TlCf8AK2y1mKGg11iWfZy8iiimSaQVX5c8euOs",
    "token_type": "bearer"
}
'''