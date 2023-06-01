from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from rotas import router

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get('/')
def get_root():
    return {'mensagem' : 'sia portal unimetrocamp'}

app.include_router(router, prefix='')

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000, log_level='info')