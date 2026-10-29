from pyspark.sql.functions import *

df = spark.read.table('err_tracks')\
               .filter(col('count').isNotNull())\
               .select(
                 col('err_type'),
                 when(col('count') == 0, 'NONE')\
                 .when(col('count').between(1,5), 'LOW')\
                 .when(col('count').between(6,20), 'MODERATE')\
                 .when(col('count').between(21,50), 'HIGH')\
                 .otherwise('CRITICAL').alias('severity_label')
                 )
