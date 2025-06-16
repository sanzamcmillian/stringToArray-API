from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Webhook(BaseModel):
    data: str


class SortedResponse(BaseModel):
    word: List[str]

@app.post("/webhook/sort-word", response_model=SortedResponse)
async def sort_word(payload: Webhook):
    if not isinstance(payload.data, str):
        raise HTTPException(status_code=400, detail="'data' must be a string")
    if payload.data is None or payload.data.strip() == "":
        return {"word": []}

    sorted_string = sorted(payload.data.lower())
    return {"word": sorted_string}