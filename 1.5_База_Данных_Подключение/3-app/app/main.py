from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI(
    title="1.5_База_Данных_Подключение third step"
)


class SHotels(BaseModel):
    adress: str
    name: str
    stars: int


@app.get("/hotels", response_model=list[SHotels])
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool]= None,
    stars: Optional[int] = Query(None, ge=1, le=5),
    ):
    hotels = [
        {
            "adress": "Granichnaya ulitsa home 40",
            "name": "My wife's family home",
            "stars": 5
        }
    ]
    return hotels


class SBookings(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_bookings(booking: SBookings):
    pass