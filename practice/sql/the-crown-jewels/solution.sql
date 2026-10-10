from pyspark.sql.functions import *


products = spark.read.table('products')
transactions = spark.read.table('transactions')

df = transactions.join(products, 'product_id', 'left')\
                 .groupBy(col('product_name'))\
                 .agg(
                   sum(col('total_amount')).alias('total_revenue')
                   )\
                 .filter(col('product_name').isNotNull())\
                 .orderBy(col('total_revenue').desc())\
                 .limit(5)
                 
display(df)
