from pyspark.sql.functions import *

customers = spark.read.table('customers')\
                      .select(
                        concat_ws(' ', col('first_name'), col('last_name')).alias('full_name'),
                        col('customer_id'),
                        col('country')
                        )\
                      .orderBy(col('full_name').asc(),col('customer_id').asc())
