from fastapi import FastAPI
import requests
from preprocessing.real_cleaning_data import preprocess
from predict.prediction import predict
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    area: int
    name: str
    property_type: str
    rooms_number: int
    zip_code: int
    land_area: int | None = None
    garden: bool | None = None
    garden_area: int | None = None
    equipped_kitchen: bool | None = None
    full_address: str | None = None
    swimming_pool: bool | None = None
    furnished: bool | None = None
    open_fire: bool | None = None
    terrace: bool | None = None
    terrace_area: int | None = None
    building_state: str


# "APARTMENT" | "HOUSE" | "OTHERS"
# "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"


@app.get("/")
async def root():
    return print("alive")


@app.post("/predict")
async def cleaning():
    return preprocess()


@app.get("/predict")
async def prediction():
    return predict()
