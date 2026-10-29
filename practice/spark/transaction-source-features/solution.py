from pyspark.sql.functions import *

df = spark.read.table('ml_features')\
               .filter(
                 (col('source') =='user_sessions') & (col('avg_val').isNull())
                 )\
               .select(
                 col('feat_name')
                 )\
               .distinct()\
               .orderBy(col('feat_name'))
