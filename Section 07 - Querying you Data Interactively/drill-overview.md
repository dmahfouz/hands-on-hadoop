# Section 07: Querying your data interactively

## Overview of Drill

### World of Hadoop - Query Engines

- Apache Drill
- Hue
- Apache Phoenix
- Presto
- Apache Zeppelin

### Apache Drill

- A technology that let's you issue SQL queries across a wide range of stuff that might be in your cluster, your wider cluster or outside your cluster
- Can issue queries across
  - MongoDB
  - HDFS
  - AWS S3
  - GCS
  - Azure Blob Storage
  - It can talk to Hive or HBase
- And unify these all into single SQL queries that can be pretty powerful

### Apache Phoenix

- Sits on top of HBase
- Although it sits on top of HBase, conceptually it is a query engine

### Presto

- Similar to Drill in that it let's you execute SQL queries across a variety of different storage technologies
- Originally created by Facebook and then open sourced
- Can talk to Cassandra (where Drill can't) and can't talk to MongoDB (where Drill can)

### Apache Drill - SQL for NoSQL

#### What is Apache Drill?

- A SQL query engine for a variety of non-relational databases and data files
  - Hive, MongoDB, HBase
  - Even flat JSON or Parquet files on HDFS, S3, Azure, Google Cloud, local file system
- Based on Google's Dremel

#### Drill - it's real SQL

- Not SQL-like
- It has a ODBC / JDBC driver so other tools can connect to it just like a relational database

#### Fast and pretty each to set up

- Important to remember these are still non-relational databases under the hood
- Allows SQL analysis of disparate data source without having to transform and load it first
  - Internally data is represented as JSON and so has no fixed schema

#### You can even do joins across different database technologies and data sources

- Or with flat JSON files that are just sitting around

#### Think of it as SQL for your *entire* ecosystem
