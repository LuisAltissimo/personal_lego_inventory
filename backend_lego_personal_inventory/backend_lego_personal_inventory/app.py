from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from backend_lego_personal_inventory.schemas import (
    Conjunto,
    Message,
    UserPublic,
    UserSchema,
)

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/conjunto', status_code=HTTPStatus.OK, response_model=Conjunto)
def read_conjunto():
    return {'conjunto': 'pantera-negra'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_users(user: UserSchema): 
    return user


@app.get('/html', response_class=HTMLResponse)
def teste():
    return """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olá mundo</title>
</head>
<body>
<h1> Olá mundo </h1>
</body>
</html>
"""
