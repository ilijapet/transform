from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, ConfigDict
from typing import List

app = FastAPI()


router = APIRouter()



class Request(BaseModel):
    model_config = ConfigDict(extra="ignore")
    text: str
    language: str | None = None 

class Reponse(BaseModel):
    token: List[str]
    count: int
    has_number: bool

@router.post("/transform")
async def transform_data(data: Request) -> Reponse:
    tokens = data.text.split()
    count = len(tokens)
    has_number = any(char.isdigit() for char in data.text)
    return Reponse(token=tokens, count=count, has_number=has_number)
    


app.include_router(router)