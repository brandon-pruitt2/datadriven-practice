from pyspark.sql.functions import * 

logs = spark.read.table('deploy_logs')\
                 .filter(
                   (col('dur_secs').isNotNull()) &
                   (upper(col('env_name')) == 'PRODUCTION') &
                   (upper(col('status')) == 'SUCCESS')
                   )\
                 .orderBy(col('dur_secs').desc(),col('deploy_at').desc())
