from pyspark.sql.functions import *

products = spark.read.table('products')
transactions = spark.read.table('transactions')

df = transactions.join(products, 'product_id', 'full')
                 .filter(col('product_name').isNotNull())
                 .groupBy(col('product_name'))\
                 .agg(
                   when(col('category') == 'Electronics',coalesce(sum(col('total_amount')),lit(0)))
                   .otherwise(lit(0)).alias('electronics_total')
                   )\
                 .orderBy(col('electronics_total').desc(),col('product_name').asc())
