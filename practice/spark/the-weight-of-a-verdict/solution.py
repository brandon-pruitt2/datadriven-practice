from pyspark.sql.functions import *

window = Window.partitionBy(col('status'))
df = spark.read.table('data_pipes')\
                .select(
                  col('pipe_id'),
                  col('pipe_name'),
                  col('status'),
                  col('rows_in'),
                  col('rows_out'),
                  col('start_at'),
                  col('dur_secs'),
                  sum(col('rows_in')).over(window).alias('status_total_rows_in')
                  )
