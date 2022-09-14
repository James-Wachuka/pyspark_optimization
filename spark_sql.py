'''
'''

import mysql.connector
import pandas as pd
from pyspark.sql import SparkSession



spark = SparkSession.builder\
.appName("sql-pyspark example").getOrCreate()

# Establish a connection
conn = mysql.connector.connect(user='root', database='lux_data_eng',
                               password='jewachu26',
                               host="localhost",
                               port=3306)


# start connection
cursor = conn.cursor()

# create a query
query = "SELECT * FROM events_"
# Create a pandas dataframe from the query
event_types_1 = pd.read_sql(query, con=conn)
#close connection
conn.close()
# Convert Pandas dataframe to spark DataFrame
result = spark.createDataFrame(event_types_1)
result.show()


'''
# using UNION function of sql to join two tables and create a df
cursor = conn.cursor()
query2= "SELECT event_type,value,time FROM events\
UNION\
    SELECT event_type,value,time FROM events_"

event_join= pd.read_sql(query2, con=conn)
#close connection
conn.close()
# Convert Pandas dataframe to spark DataFrame
result2 = spark.createDataFrame(event_join)
result2.show()'''



