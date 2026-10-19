import pandas as pd
from pyspark.sql import functions as F

file_path = "/Volumes/dev/spark_db/datasets/financialStatementCapitea.xlsx"

df_pd = pd.read_excel(file_path, engine="openpyxl")

df_spark = spark.createDataFrame(df_pd.astype(str))

df_spark_cleaned = df_spark.dropna(how="all").fillna("n.d.")

col_aktywa = [c for c in df_spark_cleaned.columns if "Aktywa" in str(c)]
col_zobowiazania = [c for c in df_spark_cleaned.columns if "Zobowiązania" in str(c)]

if col_aktywa and col_zobowiazania:
    df_spark_ratios = df_spark_cleaned.withColumn(
        "Wskaźnik_Płynności",
        F.coalesce(
            (F.col(col_aktywa[0]).cast("double") / F.col(col_zobowiazania[0]).cast("double")).cast("string"),
            F.lit("n.d.")
        )
    ).select("Wskaźnik_Płynności")
else:
    df_spark_ratios = df_spark_cleaned

display(df_spark_cleaned)
display(df_spark_ratios)

df_spark_cleaned.write.mode("overwrite").saveAsTable("dev.spark_db.capitea_data_pyspark")
df_spark_ratios.write.mode("overwrite").saveAsTable("dev.spark_db.capitea_ratios_pyspark")