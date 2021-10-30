from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

client = TestClient(app)

def test_read_main(): 
    # 测试函数是普通 def， 这样你可以用 pytest 来执行
    # 否则的话，需要使用 @pytest.mark.anyio装饰函数
    # 且 使用 from httpx import AsyncClient 定义 client
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
