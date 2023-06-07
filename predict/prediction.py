import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


def predict():
    # importer
    df = pd.read_csv("test.csv")
    # df = pd.read_json("data.json")
    
    # Defining x and y value
    X = df.drop(
        columns=[
            "price",
            "property-type",
            "equipped-kitchen",
            "full-address",
            "building-state",
        ],
        axis=1,
    )
    Y = df["price"]
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)
    regression = LinearRegression()
    regression.fit(x_train, y_train)
    prediction = print(regression.predict(x_test))
    return prediction
    # slope, intercept, r = stats.linregress(x, y)

    # # # Doing my recursive prediction function
    # return slope * x + intercept
    # print(r)

    # creating plt with two priors statements
    # mymodel = list(map(prediction, x))
    # plt.xlabel("Price by 2M€")
    # plt.ylabel("Living_area by m²")
    # plt.scatter(x, y)
    # plt.plot(x, mymodel)
    # plt.show()

    # print(r)

    # # Defining X and y
    # X = df[["area", "swimming-pool"]]
    # y = df["price"]

    # # establishing regression by X and y
    # regression = LinearRegression()
    # regression.fit(X, y)

    # # prediction + print
    # predicted = regression.predict([[200, 1]])
    # print(predicted)

    # # rajouter XText,yTest
    # regression.score(X, y)


predict()
