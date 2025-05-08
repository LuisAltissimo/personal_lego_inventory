from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session as SQLAlchemySession

from backend_lego_personal_inventory.database import get_session
from backend_lego_personal_inventory.models import User
from backend_lego_personal_inventory.routers import auth, users
from backend_lego_personal_inventory.schemas import (
    Conjunto,
    Message,
    UserPublic,
)

Session = Annotated[SQLAlchemySession, Depends(get_session)]
app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/conjunto', status_code=HTTPStatus.OK, response_model=Conjunto)
def read_conjunto():
    return {'conjunto': 'pantera-negra'}


@app.get('/html', response_class=HTMLResponse)
def teste():
    return """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""


@app.get('/users/{user_id}', response_model=UserPublic)
def ler_usuario_exercicio(
    user_id: int,
    session: Session,
):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return db_user
