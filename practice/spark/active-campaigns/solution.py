from pyspark.sql.functions import *
from pyspark.sql.types import *

df = spark.read.table('ad_impressions')\
               .groupBy(col('ad_campaign'))\
               .agg(
                 count(col('impression_id')).alias('impressions'),
                 sum(col('revenue')).alias('total_revenue'),
                 round(avg(col('clicked')*100),1).alias('ctr')
                 )\
               .filter(col('impressions')>15)\
               .orderBy(col('ctr').desc(),col('ad_campaign').asc())
               
#df = df.withColumn('ctr', round(col('clicked')/col('impressions')*100,1))
    #   .select('')
