import pandas as pd

file_path = "/Volumes/dev/spark_db/datasets/financialStatementCapitea.xlsx"

df_raw_pd = pd.read_excel(file_path)
df_cleaned_pd = df_raw_pd.dropna(how="all").fillna("n.d.")
df_ratios_pd = pd.DataFrame()

col_aktywa = [c for c in df_cleaned_pd.columns if "Aktywa" in str(c)]
col_zobowiazania = [c for c in df_cleaned_pd.columns if "Zobowiązania" in str(c)]

if col_aktywa and col_zobowiazania:
    aktywa = pd.to_numeric(df_cleaned_pd[col_aktywa[0]], errors="coerce")
    zobowiazania = pd.to_numeric(df_cleaned_pd[col_zobowiazania[0]], errors="coerce")
    df_ratios_pd["Wskaźnik_Płynności"] = (aktywa / zobowiazania).fillna("n.d.")

display(df_cleaned_pd)
display(df_ratios_pd)

spark_data_from_pd = spark.createDataFrame(df_cleaned_pd.astype(str))
spark_ratios_from_pd = spark.createDataFrame(df_ratios_pd.astype(str))

spark_data_from_pd.write.mode("overwrite").saveAsTable("dev.spark_db.capitea_data_pandas")
spark_ratios_from_pd.write.mode("overwrite").saveAsTable("dev.spark_db.capitea_ratios_pandas")