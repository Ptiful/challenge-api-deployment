import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression


def predict():
    # importer
    df = pd.read_csv("assets\cleaned_data.csv")

    # removing bedrooms, liv_room_surf, frontages, bathrooms, id, basement,elevator,
    # surroundings,flood_zone,heating, showers, toilets, furnished, energy_class, heating,flood_zone
    df = df.drop(
        columns=[
            "kitchen_type",
            "status_build",
            "bedrooms",
            "liv_room_surf",
            "frontages",
            "bathrooms",
            "id",
            "basement",
            "elevator",
            "surroundings",
            "flood_zone",
            "heating",
            "showers",
            "toilets",
            "furnished",
            "heating",
            "flood_zone",
        ]
    )

    # dropna living_area, price
    df = df.dropna(subset=["living_area", "price"])

    # replace swimming_pool None with 0
    df["swimming_pool"] = df["swimming_pool"].fillna(0)

    # "building_type",
    # "building_subtype",
    # "living_area",
    # "terrace",
    # "garden",
    # "swimming_pool",
    # "energy_class",
    # "zipcode",
    # "municipality",
    # "province",

    # print(df.isnull().sum())
    # print(df)

    # Defining x and y value
    # x = df["price"]
    # y = df["living_area"]

    # slope, intercept, r = stats.linregress(x, y)

    # # Doing my recursive prediction function
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

    # Defining X and y
    X = df[["living_area", "swimming_pool"]]
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
