from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def test ():
    return "hello world"


@app.get('/login')
def login():
    return '{name:"Rezaul", age:20}'