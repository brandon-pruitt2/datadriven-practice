from pyspark.sql.functions import *

df = spark.read.table('data_pipes')\
               .select(
                 col('pipe_name'),
                 col('start_at'),
                 when((col('rows_out')/col('rows_in')) <= 0, None)
                 .otherwise(col('rows_out')/col('rows_in')).alias('throughput_ratio')
                 )\
               .orderBy(col('pipe_name').asc(),col('start_at').asc())
