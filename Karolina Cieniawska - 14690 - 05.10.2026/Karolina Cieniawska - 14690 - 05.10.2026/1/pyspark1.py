from pyspark.sql import functions as F

df_spark = spark.table("dev.spark_db.diamonds")

df_spark.printSchema()

display(df_spark.describe())

print("KOLUMNY:", df_spark.columns)

print("LICZBA WIERSZY:", df_spark.count())

print("LICZBA UNIKALNYCH WIERSZY:", df_spark.distinct().count())

display(df_spark.select("carat", "color", "price"))

display(df_spark.limit(1000))

display(df_spark.filter((F.col("color") == "E") & (F.col("carat") > 1)))

df_spark_per_carat = df_spark.withColumn("price_per_carat", F.col("price") / F.col("carat"))
display(df_spark_per_carat.select("carat", "price", "price_per_carat"))

display(df_spark.groupBy("color").count())

display(df_spark.groupBy("clarity").agg(F.avg("price").alias("avg_price")))