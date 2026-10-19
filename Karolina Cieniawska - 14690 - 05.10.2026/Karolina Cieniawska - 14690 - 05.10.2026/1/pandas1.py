import pandas as pd

df_spark = spark.table("dev.spark_db.diamonds")
df_pd = df_spark.toPandas()

print("--- STRUKTURA DANYCH ---")
df_pd.info()

print("\n--- STATYSTYKI OPISOWE ---")
display(df_pd.describe())

print("\nKOLUMNY:", df_pd.columns.tolist())

print("\nLICZBA WIERSZY:", len(df_pd))

print("\nLICZBA UNIKALNYCH WIERSZY:", len(df_pd.drop_duplicates()))

display(df_pd[["carat", "color", "price"]])

display(df_pd.iloc[0:1000])

df_filtered_pd = df_pd[(df_pd["color"] == "E") & (df_pd["carat"] > 1)]
display(df_filtered_pd)

df_pd["price_per_carat"] = df_pd["price"] / df_pd["carat"]
display(df_pd[["carat", "price", "price_per_carat"]])

df_color_count = df_pd.groupby("color").size().reset_index(name="count")
display(df_color_count)

df_clarity_avg = df_pd.groupby("clarity")["price"].mean().reset_index(name="avg_price")
display(df_clarity_avg)