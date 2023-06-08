from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sms
import numpy as np


def predict(data):
    # importer
    train = pd.read_csv("test.csv")

    # Defining x and y value
    # X =
    # train.drop(
    X = train[
        [
            "area",
            "rooms-number",
            "zip-code",
            "land-area",
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
    # ,
    #     axis=1,
    #     errors="ignore",
    # )
    Y = train["price"]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)
    # regression = LinearRegression()
    model = sms.OLS(y_train, x_train).fit()

    # data = pd.DataFrame.to_dict(data)
    prediction = model.predict(
        [data["area"], data["equipped-kitchen"], data["swimming-pool"]]
    )

    return prediction
