from pyspark.sql.functions import *


user_sessions = spark.read.table('user_sessions')\
                          .filter((year(col('session_start'))==2026) & (col('session_duration_sec')<100))\
                          .select(
                            col('session_id'),
                            col('user_id'),
                            col('session_duration_sec')
                            )
                         
display(user_sessions)
