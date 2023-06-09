import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression


# import
train = pd.read_csv("assets/test.csv")

# Defining x and y value

X = train[
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

# ,
#     axis=1,
#     errors="ignore",
# )
Y = train["price"]
model = LinearRegression()
results = model.fit(X, Y)


filename = "model/model.sav"
pickle.dump(model, open(filename, "wb"))
