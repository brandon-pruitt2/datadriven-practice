from pyspark.sql.functions import *

df = spark.read.table('api_tokens')\
               .withColumn('issued', year(to_date(col('issued'))))\
               .filter(col('issued') == '2026')\
               .select(countDistinct(col('owner_id')).alias('distinct_owners'))
