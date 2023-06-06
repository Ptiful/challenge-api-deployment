import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression


def predict():
    # importer
    df = pd.read_csv("test.csv")

    # Defining x and y value
    x = df["price"]
    y = df["area"]

    slope, intercept, r = stats.linregress(x, y)

    # # Doing my recursive prediction function
    return slope * x + intercept
    print(r)

    # creating plt with two priors statements
    # mymodel = list(map(prediction, x))
    # plt.xlabel("Price by 2M€")
    # plt.ylabel("Living_area by m²")
    # plt.scatter(x, y)
    # plt.plot(x, mymodel)
    # plt.show()

    # print(r)

    # Defining X and y
    X = df[["area", "swimming-pool"]]
    y = df["price"]

    # establishing regression by X and y
    regression = LinearRegression()
    regression.fit(X, y)

    # prediction + print
    predicted = regression.predict([[200, 1]])
    print(predicted)

    # rajouter XText,yTest
    regression.score(X, y)


predict()
