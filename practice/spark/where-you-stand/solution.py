from pyspark.sql.functions import *

window = Window.partitionBy(col('region'))
spark.read.table('svc_health')
          .select(
            col('svc_name'),
            col('region'),
            col('latency'),
            avg('latency').over(window).alias('avg_region_latency')
            )\
          .orderBy(col('region').asc(),col('svc_name').asc(),col('latency').asc())
