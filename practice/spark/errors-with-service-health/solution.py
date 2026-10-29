from pyspark.sql.functions import *

tracks = spark.read.table('err_tracks')
health = spark.read.table('svc_health')

df = tracks.join(health, 'svc_name','inner')
           .select(
             col('err_id'),
             col('err_type'),
             col('message'),
             col('svc_name'),
             col('severity'),
             col('count'),
             col('first_at'),
             col('status'),
             col('latency').cast(DecimalType(38,3)).alias('latency'),
             col('uptime').cast(DecimalType(38,3)).alias('uptime')
             )
