from pyspark.sql.functions import *

df =spark.read.table('push_notifs')\
              .filter(
                (year(to_date(col('sent_at'))) == '2026')
                &
                (upper(col('status')) == 'DELIVERED')
                &
                (col('opened') == 1)
                
                )\
              .groupBy(lower(col('platform')).alias('platform'))\
              .agg(
                count(col('opened')).alias('opened_count')
                )\
              .orderBy(col('opened_count').desc())
