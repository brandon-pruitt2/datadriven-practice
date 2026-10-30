from pyspark.sql.functions import *

w = Window.partitionBy("user_id").orderBy("txn_date")

df = (
  spark.read.table("transactions")
  .select("user_id", to_date("transaction_date").alias("txn_date"))
  .withColumn("gap_days", datediff("txn_date", F.lag("txn_date").over(w)))
  .filter(col("gap_days").between(65, 80))
  .select("user_id")
  .distinct()
  .orderBy("user_id")
)
