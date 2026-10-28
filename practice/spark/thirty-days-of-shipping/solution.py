from pyspark.sql import functions as F

logs = (
  spark.read.table("deploy_logs")
  .withColumn("deploy_ts", F.to_timestamp("deploy_at", "yyyy-MM-dd HH:mm:ss"))
  .groupBy(
    F.date_format("deploy_ts", "yyyy-MM").alias("deploy_month"),
  )
  .agg(F.countDistinct("svc_name", "version").alias("deployments"))
)
