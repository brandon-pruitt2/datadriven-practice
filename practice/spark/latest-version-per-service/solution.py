from pyspark.sql.functions import *

window = Window.partitionBy('svc_name','version').orderBy(col('deploy_at').desc())
logs = spark.read.table('deploy_logs')\
                 .withColumn('rn', row_number().over(window))\
                 .filter(col('rn') ==1)\
                 .select(
                   'svc_name',
                   'version',
                   'dur_secs'
                   )\
