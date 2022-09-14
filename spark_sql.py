'''
PySpark SQL is a module in Spark which integrates relational 
processing with Spark's functional programming API.
We can extract the data by using an SQL query language.
We can use the queries same as the SQL language
'''

import mysql.connector
import pandas as pd
from pyspark.sql import SparkSession
import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


spark = SparkSession.builder\
.appName("sql-pyspark example").getOrCreate()

# Establish a connection
conn = mysql.connector.connect(user='root', database='lux_data_eng',
                               password='',
                               host="localhost",
                               port=3306)


# start connection
cursor = conn.cursor()


# create a query
query = "SELECT * FROM events_ GROUP BY (event_type)"
# Create a pandas dataframe from the query
event_types_1 = pd.read_sql(query, con=conn)
#close connection
# Convert Pandas dataframe to spark DataFrame
result = spark.createDataFrame(event_types_1)
result.show()



# using UNION function of sql to join two tables and create a df
# start-connection

query2= "SELECT event_type,value,time FROM events UNION SELECT event_type,value,time FROM events_"

event_join= pd.read_sql(query2, con=conn)
#close connection 
conn.close()
# Convert Pandas dataframe to spark DataFrame
result2 = spark.createDataFrame(event_join)
result2.show()



