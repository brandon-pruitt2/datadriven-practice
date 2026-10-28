from pyspark.sql.functions import *
chat = spark.read.table('chat_msgs')
                 .withColumn("word_count",
                   when(col("content").isNotNull(), size(split("content", " "))))\
  
                 .select(
                       col('msg_id'),
                       col('word_count')
                   )
