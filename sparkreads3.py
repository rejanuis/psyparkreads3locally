from pyspark.sql import SparkSession
from pyspark import SparkConf

# initialization spark conf for set configurations to spark
conf = SparkConf()

# set jar file for library that used to connect s3
conf.set('spark.packages.jars', 'org.apache.hadoop:hadoop-aws:2.7.0')
conf.set('spark.packages.jars', 'com.amazonaws:aws-java-sdk:1.7.4')

# these for configuration your hadoop file using filesystem read s3
conf.set('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')

# these for configuration for providing credetial aws s3
conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider')

# set endpoint or region that bucket you already created in aws s3
conf.set('spark.hadoop.fs.s3a.endpoint', 's3.ap-southeast-1.amazonaws.com')

# put your aws access key and secret key here
conf.set('spark.hadoop.fs.s3a.access.key', 'YOUR ACCESS KEY')
conf.set('spark.hadoop.fs.s3a.secret.key', 'YOUR SECRET KEY')

# example initialization spark
spark = SparkSession.builder.config(conf=conf).master("local[1]").appName('sparktest').getOrCreate()

# this sample read parquet file from s3, you can modify as you want it cheers
df_silver = spark.read.parquet('s3a://YOUR_BUCKET/YOUR FILE PARQUET.parquet')
