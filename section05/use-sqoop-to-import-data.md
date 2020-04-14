# Section 05: Using relational data stores with Hadoop

## Activity: Use Sqoop to export data from Hadoop to MySQL

1. Sign into mysql cli

    ```sh
    mysql -u root -p <password>
    ```

2. Grant necessary priviledges

    ```sql
    GRANT ALL PRIVILEGES ON movielens.* to ''@'localhost';
    ```

    **Note for HDP >= 2.6.5:**
    The above command will not work. Instead, use:

    ```sql
    GRANT ALL PRIVILEGES ON movielens.* to root@localhost identified by 'hadoop';
    ```

3. Import data to HDFS

    ```sh
    sqoop import \
        --username root -P \
        --connect jdbc:mysql://localhost/movielens \
        --driver com.mysql.jdbc.Driver \
        --table movies -m 1
    ```

    **Note**: When prompted, **enter password for mysql user** (in this case 'hadoop'), not HDFS cli user.

4. Import data to Hive (requires additional `--hive-import` parameter)

    ```sh
    sqoop import \
        --username root -P \
        --connect jdbc:mysql://localhost/movielens \
        --driver com.mysql.jdbc.Driver \
        --table movies -m 1 \
        --hive-import
    ```
