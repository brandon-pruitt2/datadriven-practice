from pyspark.sql.functions import *
from pyspark.sql.types import *
window = Window.partitionBy().orderBy(col('duration_seconds').desc())
df = spark.read.table('content_items')\
               .select(
                 col('content_id'),
                 col('title'),
                 col('content_type'),
                 col('duration_seconds'),
                 col('creator_id'),
                 col('publish_date'),
                 col('duration_seconds').cast(DecimalType(38,2)).alias('duration_decimal'),
                 abs(col('duration_seconds')-max('duration_seconds').over(window)).cast(DecimalType(38,2)).alias('diff_from_longest')
                 ).orderBy(col('content_id').asc())
