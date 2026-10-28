from pyspark.sql.functions import *

products = spark.read.table('products')
transactions = spark.read.table('transactions')

df = products.join(transactions, 'product_id', 'left')
                 .filter(col('product_name').isNotNull())
                 .groupBy(col('product_name'))\
                 .agg(
                  coalesce(
                     sum(F.when(F.col("category") == "Electronics", F.col("total_amount"))),
                     lit(0)
                    ).alias("electronics_total")
  )\
                 .orderBy(col('electronics_total').desc(),col('product_name').asc())
