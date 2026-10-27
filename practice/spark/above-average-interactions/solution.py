from pyspark.sql import Window
from pyspark.sql.functions import avg, col, count

df_result = (
  spark.read.table("user_sessions")
  .groupBy("user_id")
  .agg(count("session_id").alias("total_sessions"))
  .withColumn("avg_sessions", avg("total_sessions").over(Window.partitionBy()))
  .filter(col("total_sessions") > col("avg_sessions"))
  .select("user_id", "total_sessions")
)

df_result.show()
