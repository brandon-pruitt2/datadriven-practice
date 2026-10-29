from pyspark.sql.functions import *

users = spark.read.table('users')\
                  .withColumn('signup_year', year(to_date(col('signup_date'))))\
                  .filter(month(to_date(col('signup_date'))).between(1,7))\
                  .groupBy('signup_year')\
                  .agg(
                    count(col('user_id')).alias('signup_count')
                    )\
                  .orderBy(col('signup_year').asc())
