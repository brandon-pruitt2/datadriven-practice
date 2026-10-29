from pyspark.sql.functions import *

spark.read.table('alert_events')\
          .filter(
            (year(to_date(col('fired_at'))) == '2026') &
            ((upper(col('severity')) == 'HIGH') | (upper(col('severity')) == 'CRITICAL') )
            )
