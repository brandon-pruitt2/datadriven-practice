from pyspark.sql.functions import *
chat = spark.read.table('chat_msgs')
                 .withColumn("word_count",
                  length('content') - length(regexp_replace('content',' ', ''))+1)
                 .select(
                       col('msg_id'),
                       col('word_count')
                   )
