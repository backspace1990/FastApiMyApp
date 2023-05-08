from fastapi import FastAPI, Query
from typing import Optional
from datetime import date

app = FastAPI(
    title="1.4_Валидация_данных_с_Pydantic second step"
)


@app.get("/hotels")
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool]= None,
    stars: Optional[int] = Query(None, ge=1, le=5),
    ):
    return date_from, date_to