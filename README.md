##### CACHE() VS PERSIT
For (interactive and iterative) Spark calculations, optimization strategies like caching or persistence are used. They assist in preserving interim partial results for reuse in later phases. Thus, these interim results as RDDs are copied, stored on disk, or maintained in memory (the default).

Both persist() and cache() are the Spark optimization technique, used to store the data, but only difference is cache() method by default stores the data in-memory (MEMORY_ONLY) whereas in persist() method developer can define the storage level to in-memory or in-disk.

using cache()
```
df1.cache()
````
using persist
```
df1.persist(pyspark.StorageLevel.MEMORY_ONLY)
```
Using cache() and persist() methods, Spark provides an optimization mechanism to store the intermediate computation of a Spark DataFrame so they can be reused in subsequent actions.When you persist a dataset, each node stores its partitioned data in memory and reuses them in other actions on that dataset. And Spark’s persisted data on nodes are fault-tolerant meaning if any partition of a Dataset is lost, it will automatically be recomputed using the original transformations that created it.

##### OUTPUT
There is reduced time of execution when doing operation on cached dataframe compared to the non-persisted dataframe

```cached df = 111ms```

```non-persited df = 375 ms```


##### SPARK-SQL
PySpark SQL is a module in Spark which integrates relational processing with Spark's functional programming API.
We can extract the data by using an SQL query language.We can use the queries same as the SQL language.
Mysql connector is used to connect to the database. The query below retrieves data from ```events_```  and ```events``` table of ```lux_data_eng``` database. Using the created connection and creates a UNION of the two tables

Pyspark is used to covert the pandas dataframe to a spark dataframe , which shows the result of query.

##### USAGE
clone the repository,activate the python venv,install the requirements,run the scripts





