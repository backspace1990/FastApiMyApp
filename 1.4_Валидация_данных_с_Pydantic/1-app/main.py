from fastapi import FastAPI
from datetime import date


app = FastAPI(
    title="1.4_Валидация_данных_с_Pydantic first step"
)


@app.get("/hotels/{hotel_id}")
def get_hotels(hotel_id: int, date_from: date, date_to: date):
    return f"Five-Star Hotels id: {hotel_id} date_from: {date_from}, date_to: {date_to}"