import pandas as pd
import pickle


with open("model/model.sav", "rb") as f:
    model = pickle.load(f)


def predict(data):
    result = model.predict(data)

    print(result)
    return result
