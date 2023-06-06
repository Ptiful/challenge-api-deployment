from fastapi import FastAPI
import requests
from preprocessing import cleaning_data
from predict import prediction

app = FastAPI()


@app.get("/")
async def root():
    response = requests.get("http://127.0.0.1:8000/")
    if response == 200:
        return print("alive")
    else:
        print("Server is out there but not with us")

@app.post("/predict")
async def cleaning(area:int, property_type="" ,rooms_number = int,zipcode = int,
                    land_area:int=0,garden:bool = "" ,garden_area:int =0,equipped_kitchen:bool ="",
                    full_address:str ="",swimming_pool:bool = "",furnished:bool = "",
                    open_fire:bool = "",terrace:bool = "", terrace_area:int = "",
                    facades_number:int = "", building_state:""):
    return preprocess()

@app.get("/predict")
async def prediction():
    return predict()
    

    {
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}
