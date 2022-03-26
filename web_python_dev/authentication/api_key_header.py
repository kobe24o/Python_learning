# _*_ coding: utf-8 _*_
# @Time : 2022/3/25 15:31
# @Author : Michael
# @File : api_key_header.py
# @desc :

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_TOKEN = "iam_mi_ma" # 假装是一个密码
app = FastAPI()

async def api_token(token: str=Depends(APIKeyHeader(name='token'))):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

@app.get('/protected-route', dependencies=[Depends(api_token)])
async def protected_route():
    return {"hello": "michael"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_key_header:app", host="127.0.0.1", port=8001, reload=True, debug=True)