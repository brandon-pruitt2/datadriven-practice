from pyspark.sql.functions import *

items = spark.read.table('content_items')\
                  .groupBy('content_type')\
                  .agg(
                    count('content_id').alias('item_count')
                    )\
                  .orderBy('content_type')
