from typing import Optional
from fastapi import FastAPI, Depends, Cookie

app = FastAPI()

def query_extractor(q: Optional[str] = None):
    print("run one time！")
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    print("run flag！")
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor),
                    another_query: str = Depends(query_extractor, use_cache=False)):
    return {"q_or_cookie": query_or_default}