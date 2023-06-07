import pandas as pd
import re
import numpy as np


def preprocess():
    df = pd.read_csv("assets/immoweb_properties_data.csv", engine="python")

    df = df[df["url"].str.contains("new-real-estate-project") == False]
    df.rename(
        columns={
            "Living area": "area",
            "Address": "full-address",
            "Garden surface": "garden-area",
            "Terrace surface": "terrace-area",
            "Garden": "garden",
            "Garden surface": "garden-area",
            "Swimming pool": "swimming-pool",
            "Kitchen type": "equipped-kitchen",
            "Furnished": "furnished",
            "How many fireplaces?": "open-fire",
            "Terrace": "terrace",
            "Number of frontages": "facades-number",
            "Building condition": "building-state",
            "Bedrooms": "rooms-number",
            "Surface of the plot": "land-area",
            "Price": "price",
        },
        inplace=True,
    )
    df["zip-code"] = df["url"].str.extract(r"([0-9]{1,5})").astype(int)
    df["property-type"] = df["url"].str.split("/").str[5]

    df = df[
        [
            "area",
            "property-type",
            "price",
            "rooms-number",
            "zip-code",
            "land-area",
            "garden",
            "garden-area",
            "equipped-kitchen",
            "full-address",
            "swimming-pool",
            "furnished",
            "open-fire",
            "terrace",
            "terrace-area",
            "facades-number",
            "building-state",
        ]
    ]

    df["terrace"] = df["terrace"].replace("Yes", 1).fillna(0)
    df["terrace-area"] = df["terrace-area"].str.extract(r"([0-9]{1,3})").astype(float)
    # df["terrace"] = df[["terrace", "terrace-area"]].sum(axis=1, skipna=False).fillna(0)
    df["area"] = df["area"].str.extract(r"([0-9]{1,5})").astype(float)
    df["garden"] = df["garden"].replace("Yes", 1).fillna(0)
    df["garden-area"] = df["garden-area"].str.extract(r"([0-9]{2,5})").astype(float)
    df["garden-area"] = df["garden-area"].fillna(0)
    df["land-area"] = df["land-area"].str.extract(r"([0-9]{1,7})").astype(float)
    df["land-area"] = df["land-area"].fillna(0)
    df["rooms-number"] = df["rooms-number"].fillna(0)
    df["swimming-pool"] = df["swimming-pool"].replace(["Yes", "No"], [1, 0]).fillna(0)
    df["furnished"] = df["furnished"].replace(["Yes", "No"], [1, 0])
    df["open-fire"] = df["open-fire"].replace(1.0, 1).fillna(0)
    df["terrace"] = df["terrace"].replace(1.0, 1).fillna(0)
    df["terrace-area"] = df["terrace-area"].fillna(0)
    df["furnished"] = df["furnished"].fillna(0)
    df["price"] = df["price"].str.extract(r"([0-9]{4,7})").astype(float)
    df["facades-number"] = df["facades-number"].fillna(0)
    df["equipped-kitchen"] = df["equipped-kitchen"].fillna(0)
    df["price"].replace("", np.nan, inplace=True)
    df["building-state"].replace("", np.nan, inplace=True)
    df["full-address"].replace("", np.nan, inplace=True)
    df["area"].replace("", np.nan, inplace=True)
    df.dropna(subset=["price", "building-state", "full-address", "area"], inplace=True)

    print(df.isnull().sum())

    return df.to_csv("test.csv")


preprocess()
