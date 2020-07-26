# Section 07: Querying your data interactively

## Activity: Query both Cassandra and Hive using Presto

1. SSH into HDP, login as super user using `su root`

2. Start Cassandra using:

    ```sh
    service cassandra start
    ```

3. Enable the thrift service on Cassandra:

    ```sh
    nodetool enablethrift
    ```

    Enable Cassandra cql shell:

    `cqlsh --cqlversion="3.4.0"`

4. In `cqlsh`, list keyspaces (dbs) using:

    ```sql
    describe keyspaces;
    ```

5. Check `user` table is there and has data

    ```sql
    use movielens;
    describe tables;
    select * from users limit 10;
    ```

6. Connect the `users` table from Cassandra with the ratings data in Hive with Presto so that data from Cassandra and Hive can be merged together

    - 6.1. Configure properties for Cassandra in Presto

    ```sh
    cd /home/maria_dev/presto-server-0.234/etc/catalog
    ```

    Run `vi cassandra.properties` to create a cassandra.properties file containing the following:

    ```properties
    # cassandra.properties
    # name to connector
    connector.name=cassandra 
    # contact points
    cassandra.contact-points=127.0.0.1
    ```

    - 6.2. Go back to top level of the presto server directory using `cd ../..` and start the presto server:

    ```sh
    bin/launcher start
    ```

7. Connect to both hive and cassandra at the same time using the following:

    ```sh
    ```

8. Check cassandra movielens table can be accessed from the presto-cli

    ```sql
    show tables from cassandra.movielens;
    ```

    Which should return a `users` table (1 row)

9. Describe users table

    ```sql
    describe cassandra.movielens.users;
    ```

10. Query cassandra db to show top 10 rows of users table

    ```sql
    select * from cassandra.movielens.users limit 10;
    ```

11. In the same session, query the hive ratings table (*nb: check hive view in Ambari to check if ratings table is in movielens db*):

    ```sql
    select * from hive.movielens.ratings limit 10;
    ```

12. Join hive `ratings` table with the cassandra `users` table:

    ```sql
    select u.occupation, count(*)
    from hive.movielens.ratings r
    join cassandra.movielens.users u
    on r.user_id = u.user_id
    group by u.occupation;
    ```

13. Connect to different dbs and sources on https://prestodb.io/docs/current/connector/index.html (e.g. '/mongodb/index.html')

14. Clean up

    Quit presto-cli:

    ```sh
    quit
    ```

    Stop Presto server using:

    ```sh
    bin/launcher stop
    ```

    Stop cassandra

    ```sh
    service cassandra stop
    ```

