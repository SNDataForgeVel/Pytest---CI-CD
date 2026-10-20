from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,inline,col
from CommonLib import *
spark = SparkSession.builder.appName("Products").getOrCreate()
Products = spark.read.json(r"./SampleFile/Products_Formatted.json",
                                multiLine="true"
                          )
Products = FilterRows(
                        Products.select(inline("Products")),
                        "ProductId",
                        "NULL",
                        "=="
                      )