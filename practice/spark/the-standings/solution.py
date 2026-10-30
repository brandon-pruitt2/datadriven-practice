from pyspark.sql.functions import *

products = spark.read.table('products')
transactions = spark.read.table('transactions')

window = Window.partitionBy().orderBy(col('total_units').desc())
df = transactions.join(broadcast(products), 'product_id', 'inner')\
             .groupBy(col('category'))\
             .agg(
               sum(col('total_amount')).alias('total_revenue'),
               sum(col('quantity')).alias('total_units')
               )\
             .select(
               col('category'),
               col('total_revenue'),
               col('total_units'),
               rank().over(window).alias('position')
               )\
             .orderBy(col('total_units').desc())
