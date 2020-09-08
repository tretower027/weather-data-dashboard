import pandas as pd

weather_df = pd.read_csv("cities.csv")

weather_df.to_html("table.html", index=False, classes=["table", "table-striped", "table-hover"])