# ​Table of contents 

1. **Presentation** *(Guillaume)*
2. **Installation**  
2.1. Mac *(Luca)*  
2.2. Linux / Windows via WLS *(Guillaume)*  
2.3. Windows *(Quentin)*
3. **Tutorial / Main existing commands** *(Quentin)*
4. **Use case** *(Luca)*
5. **Performance Analysis** *(Matthieu)*  
5.1. Pros of Redis  
5.2. Cons of Redis
6. **Redis comparison with the others**  
6.1. Advantages  
6.2. Inconvenients
7. **Conclusion**

## Presentation
## Installation
### Mac
### Linux / Windows via WLS
### Windows
## Tutorial / Main existing commands
## Use case
## Performance Analysis
### Pros of Redis
### Cons of Redis

|Framwork | PRO | CONS
------ | ---|-----
   __Cassandra__ | - fully distributed database update nodes with rolling restarts <br><br>-Linear scalability the same application can scale from laptop to a webservice with billions of rows in a table<br><br>-Amazing performance you can get answers in milliseconds. Cassandra excels at recording, processing, and retrieving time-series data.|-Cassandra runs on the JVM and therefor may require a lot of GC tuning for read/write intensive applications.<br><br>-Requires manual periodic maintenance - for example it is recommended to run a cleanup on a regular basis.<br><br>-There are a lot of knobs and buttons to configure the system. For many cases the default configuration will be sufficient, but if it’s not - you will need significant ramp up on the inner workings of Cassandra in order to effectively tune it. 
  __MongoDB__     | -Easy to learn you can figure out how to use MongoDB pretty fast.<br><br>-Fast performance. lots of ready-made solutions out there.<br><br>-There's a lot of support in the existing ecosystem Query syntax is pretty simple to grasp and utilize.<br><br>-Aggregate functions are powerful. Scaling options. Documentation is quite good and versioned for each release.<br><br>-Horizontally scalable database Performance is very high   | -An aggregate pipeline can be a bit overwhelming as a newcomer.<br><br>-There's still no real concept of joins with references/foreign keys, although the aggregate framework has a feature that is close. <br><br>-Database management/dev ops can still be time-consuming if rolling your own deployments.<br><br>-Doesn’t support joins Data Size is High Nesting of documents is limited Increase unnecessary usage of memory By design, joined collections tend to be much slower than in relational DB. 
  __Neo4j__   | -Neo4j is fast.<br><br>-Neo4j has its own query language CYPHER which is very intuitive and easy to use.<br><br>-Neo4j supports API in almost every language like Java, Python, PHP, NodeJS Easy way to query data.<br><br>-Easy way to insert and store relationships.  <br><br>-Easy to visualize data in Neo4j browser. <br><br>-Easy to learn.       |  -Doesn't have native support for complex properties for nodes and relationships <br><br>-Sometimes hard to visualize complex data analyses. <br><br>-Tough to see space used. <br><br>-Tough to allocate memory or other configurations. <br><br>-not easy to configure for a large dataset graphic <br><br>-not clear for complex dataset in which more than 10 relation possible graphs are not good Also the interactive UI for a complex dataset is little bit complex 
__Redis__ |-Easy for developers to understand. <br><br>-Reliable. With a proper multi-node configuration, it can handle failover instantly. <br><br>-Configurable uses Redis for both long-term storage and temporary expiry keys without taking on another external dependency. <br><br>-Fast tens of thousands of RPS and it doesn't skip a beat. Supports a huge variety of data types <br><br>-Easy to install Operations are atomic Multi-utility tool (used in a number of use cases)  | -Some difficulty scaling Redis without it becoming prohibitively expensive. <br><br>-Redis has very simple search capabilities, which means it’s not suitable for all use cases. <br><br>-Redis doesn't have good native support for storing data in object form and many libraries built over it return data as a string, meaning you need build your own serialization layer over it.<br><br>-Doesn’t support joins Knowledge required of Lua for stored procedures the dataset has to fit comfortably in memory 


## Redis comparison with the others
### Advantages
### Inconvenients
## Conclusion
