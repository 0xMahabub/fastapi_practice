from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return "Hello! FastAPI"



@app.get('/dic')
def index():
    return { 'msg': { 'name': 'Mahabub' } }