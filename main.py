from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return "Hello! FastAPI"


# returning dictionary => will be recieved as JSON
@app.get('/dic')
def index():
    return { 'msg': { 'name': 'Mahabub' } }


# using dynamic route
@app.get('/r/{id}')
def index(id):
    return { 'r': id }

@app.get('/rt/{id}')
def index(id: int):
    return { 'r': id }