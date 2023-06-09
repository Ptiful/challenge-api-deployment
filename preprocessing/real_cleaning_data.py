import pandas as pd
import re
import numpy as np


def preprocess(json_data):
    print(json_data)
    df = pd.DataFrame(json_data, index=[0])
    print(df)

    # df = df[df["url"].str.contains("new-real-estate-project") == False]
    # df.rename(
    #     columns={
    #         "Living area": "area",
    #         "Address": "full_address",
    #         "Garden surface": "garden_area",
    #         "Terrace surface": "terrace_area",
    #         "Garden": "garden",
    #         "Garden surface": "garden_area",
    #         "Swimming pool": "swimming_pool",
    #         "Kitchen type": "equipped_kitchen",
    #         "Furnished": "furnished",
    #         "How many fireplaces?": "open_fire",
    #         "Terrace": "terrace",
    #         "Number of frontages": "facades_number",
    #         "Building condition": "building_state",
    #         "Bedrooms": "rooms_number",
    #         "Surface of the plot": "land_area",
    #         "Price": "price",
    #     },
    #     inplace=True,
    # )
    # df["zip_code"] = df["url"].str.extract(r"([0-9]{1,5})").astype(int)
    # df["property_type"] = df["url"].str.split("/").str[5]

    df = df[
        [
            "area",
            "property_type",
            "rooms_number",
            "zip_code",
            "land_area",
            "garden",
            "garden_area",
            "equipped_kitchen",
            "full_address",
            "swimming_pool",
            "furnished",
            "open_fire",
            "terrace",
            "terrace_area",
            "building_state",
        ]
    ]

    # df["terrace"] = df["terrace"].replace("Yes", 1).fillna(0)
    # # df["terrace_area"] = df["terrace_area"].str.extract(r"([0-9]{1,3})").astype(int)
    # # df["terrace"] = df[["terrace", "terrace-area"]].sum(axis=1, skipna=False).fillna(0)
    # df["area"] = df["area"].str.extract(r"([0-9]{1,5})").astype(float)
    # df["garden"] = df["garden"].replace("Yes", 1).fillna(0)
    # df["garden-area"] = df["garden_area"].str.extract(r"([0-9]{2,5})").astype(float)
    # df["garden_area"] = df["garden_area"].fillna(0)
    # df["land_area"] = df["land_area"].str.extract(r"([0-9]{1,7})").astype(float)
    # df["land_area"] = df["land_area"].fillna(0)
    # df["rooms_number"] = df["rooms_number"].fillna(0)
    # df["swimming_pool"] = df["swimming_pool"].replace(["Yes", "No"], [1, 0]).fillna(0)
    # df["furnished"] = df["furnished"].replace(["Yes", "No"], [1, 0])
    # df["open_fire"] = df["open_fire"].replace(1.0, 1).fillna(0)
    # df["terrace"] = df["terrace"].replace(1.0, 1).fillna(0)
    # df["terrace_area"] = df["terrace_area"].fillna(0)
    # df["furnished"] = df["furnished"].fillna(0)
    # df["price"] = df["price"].str.extract(r"([0-9]{4,7})").astype(float)
    # df["facades_number"] = df["facades_number"].fillna(0)
    # df["equipped_kitchen"] = df["equipped_kitchen"].fillna(0)
    # df["price"].replace("", np.nan, inplace=True)
    # df["building_state"].replace("", np.nan, inplace=True)
    # df["full_address"].replace("", np.nan, inplace=True)
    # df["area"].replace("", np.nan, inplace=True)
    # df.dropna(subset=["price", "building_state", "full_address", "area"], inplace=True)
    print(df.isnull().sum())
    print("cleaned", df)
    df = df[
        [
            "area",
            "rooms_number",
            # "zip-code",
            "land_area",
            # "garden",
            # "garden-area",
            # "equipped-kitchen",
            # "full-address",
            # "swimming-pool",
            # "furnished",
            # "open-fire",
            # "terrace",
            # "terrace-area",
            # "facades-number",
            # "building-state",
        ]
    ]
    return df


# preprocess()
