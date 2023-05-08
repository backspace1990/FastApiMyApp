from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI(
    title="1.4_Валидация_данных_с_Pydantic third step"
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


class SBookings(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_bookings(booking: SBookings):
    pass