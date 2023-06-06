import pandas as pd

df = pd.read_csv("assets/immoweb_properties_data.csv")

df["property-type"] = df["url"].str.split("/").str[5]
print(df["property-type"])
