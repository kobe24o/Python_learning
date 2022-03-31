# _*_ coding: utf-8 _*_
# @Time : 2022/3/25 19:30
# @Author : Michael
# @File : app.py
# @desc :

from tortoise import timezone
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist, IntegrityError
from typing import cast
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from web_python_dev.authentication.email_sys.models import User, UserCreate, UserDB, UserTortoise, AccessTokenTortoise
from web_python_dev.authentication.email_sys.authentication import authenticate, create_access_token
from web_python_dev.authentication.email_sys.password import get_password_hash

app = FastAPI()

TORTOISE_ORM = {
    'connections': {'default': 'sqlite://cp7_emailsys.db'},
    'apps': {
        'models': {
            'models': ['web_python_dev.authentication.email_sys.models'],
            'default_connection': 'default',
        }
    },
    'use_tz': True,
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl='token')))->UserTortoise:
    try:
        access_token: AccessTokenTortoise = await AccessTokenTortoise.get(access_token=token, expiration_date__gte=timezone.now()).select_related('user_col')
        return cast(UserTortoise, access_token.user_col)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

@app.post('/register', status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate)->User:
    hashed_password = get_password_hash(user.password)
    try:
        user_tortoise = await UserTortoise.create(**user.dict(), hashed_password=hashed_password)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User email already exists')
    return User.from_orm(user_tortoise)

@app.post('/token')
async def create_token(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)):
    email = form_data.username
    password = form_data.password
    user = await authenticate(email, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = await create_access_token(user)
    return {'access_token': token.access_token, 'token_type': 'bearer'}

@app.get('/protected-route', response_model=User)
async def protected_route(user: UserDB = Depends(get_current_user)):
    return User.from_orm(user)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host='127.0.0.1', port=8001, reload=True, debug=True)