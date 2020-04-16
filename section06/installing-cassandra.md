# Using non-relational data stores with Hadoop

## Installing Cassandra

- Note: Cassandra requires Python 2.7 (Python 2.6 included in HDP:v2.5 and Python27 included in HDP:v2.65)

- If using HDP 2.5.0 then Python needs to be updated to v2.7 without break the OS (CentOS which relies on Python 2.6) -- not covered here!

1. Login as super user `su root` with root `$pwd`

2. [B] (Optional) - Update yum using `yum update`

3. Change directory using/to: `cd /etc/yum.repos.d`

#TODO: Finish!

4. Run Spark Job

    Use the following:

    ```sh
    spark-submit --packages datastax:spark-cassandra-connector:2.4.0-s_2.11 CassandraSpark.py
    ```

    Instead of:

    ```sh
    spark-submit --packages datastax:spark-cassandra-connector:2.0.0-M2-s_2.11 CassandraSpark.py
    ```
