# Section 07: Querying your Data interactively

## Presto overview - distributing queries across different data stores

### What is Presto

- It's a lot like Drill
  - *It can connect to many different "big data" databases and data stores at once, and query across them*
    - This can include MongoDB, Cassandra, Hive, etc
    - Presto provides a single point of access for issuing queries across multiple data stores in an organisation that contains huge amounts of data that are scaled horizontally on different systems
    - This means that like Drill, you can issue queries across those different databases and join them together for more complex queries
  - *Familiar SQL syntax*
    - Although not a database itself, it is a layer between your SQL queries and various data stores distributed throughout your organisation
  - *Optimised for OLAP - analytic queries, data warehousing*
    - Not meant for high transactions or being super quick in latency
- Developed and still partially maintained by Facebook
- Exposes JDBC (driver), command-line and Tableau interfaces
  - This means you can connect existing applications that talk to SQL pretty easily through Presto to you entire data ecosystem internally, no matter how big and complex it may be

### Why Presto

- Vs. Drill? It has a Cassandra connector
- If it's good enough for Facebook...
  - *"Facebook uses Presto for interactive queries against serveral internal data stores, including their 300PB data warehouse. Over 1,000 Facebook employees use Presto daily to run more than 30,000 queries that in total scan over a petabyte each per data"
  - Also used by Dropbox and AirBnb
- *"A single Presto query can combine data from multiple sources, allowing for analytics across your entire organisation"*
- *"Presto breaks the false choice between having fast analytics using an expensive commercial solution or using a slow "free" solution that requires excessive hardware"*

### What can Presto connect to?

- Cassandra (also created by Facebook)
- Hive
- MongoDB
- MySQL
- Local files
- \+ Others
  - Kafka
  - JMX
  - PostgreSQL
  - Redis
  - Accumulo
