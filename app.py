from fastapi import FastAPI
from preprocessing.real_cleaning_data import preprocess
from predict.prediction import predict
from pydantic import BaseModel
from typing import Literal
import json


app = FastAPI()


class Item(BaseModel):
    area: int
    property_type: Literal["APARTMENT", "HOUSE", "OTHERS"]
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
    building_state: Literal[
        "NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"
    ]


@app.get("/")
async def root():
    a = print("alive")
    return a


@app.post("/predict")
async def prediction(item: Item):
    data = {
        "area": item.area,
        "property-type": item.property_type,
        "rooms_number": item.rooms_number,
        "zip-code": item.zip_code,
        "land-area": item.land_area,
        "item.garden": item.garden,
        "garden-area": item.garden_area,
        "equipped-kitchen": item.equipped_kitchen,
        "full-address": item.full_address,
        "swimming-pool": item.swimming_pool,
        "furnished": item.furnished,
        "open-fire": item.open_fire,
        "terrace": item.terrace,
        "terrace-area": item.terrace_area,
        "building-stat": item.building_state,
    }
    with open("data.json", "w") as f:
        json.dump(data, f)
    return print(predict)
