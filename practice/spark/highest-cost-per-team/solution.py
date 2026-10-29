from pyspark.sql.functions import *
from pyspark.sql.types import *

df = spark.read.table('cost_allocs')\
               .groupBy(lower(col('team_name')).alias('team_name'))\
               .agg(
                 max(col('amount')).cast(DecimalType(38,3)).alias('max_amount')
                 )\
               .orderBy(col('max_amount').desc())
