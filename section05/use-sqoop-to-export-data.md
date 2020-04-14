# Section 05: Using relational data stores with Hadoop

## Activity: Use Sqoop to export data from Hadoop to MySQL

1. Goto `/apps/hive/warehouse/movies/part-m-00000` to view the data from which the movies table from hive is stored

    NB: On other distributions it might be `/users/hive` or `/user/hive` but on Hortonworks it is `/apps/hive/`.

2. Make sure table exists ahead of time in mysql

    - Log into mysql

    ```sh
    mysql -u root -p $pwd
    ```

    - Change to `movielens` database

    ```sql
    mysql> use movielens;
    ```

    - Create table to store movie data

    ```sql
    mysql> CREATE TABLE exported_movies (
        id INTEGER,
        title VARCHAR(255),
        releaseDate DATE);
    ```

    - Finally, exit

    ```sql
    mysql> exit
    ```

3. Export the data using sqoop

    ```sh
    sqoop export \
        --connect jdbc:mysql://localhost/movielens -m 1 \
        --driver com.mysql.jdbc.Driver \
        --table exported_movies \
        --export-dir /apps/hive/warehouse/movies \
        --input-fields-terminated-by '\0001' \
        --username root -P
    ```

    - (Commented version:)

    ```sh
    sqoop export \
        # connect to movielens db on mysql running on local host
        # (with 1 mapper)
        --connect jdbc:mysql://localhost/movielens -m 1 \
        # using specified jdbc driver
        --driver com.mysql.jdbc.Driver \
        # using table created before
        --table exported_movies \
        # where it's going to get the data from, i.e.:
        # the location of the export directory being
        # where data is stored in hive data warehouse
        --export-dir /apps/hive/warehouse/movies \
        # terminated (delimited) by ascii character 1
        --input-fields-terminated-by '\0001' \
        # for user 'root' and with password to be specified
        --username root -P
    ```

4. View data in mysql

    - Log into mysql

        ```sh
        mysql -u root -p $pwd
        ```

    - Go to `movielens` database

        ```sql
        mysql> use movielens;
        ```

    - Query new table

        ```sql
        mysql> SELECT * from exported_movies LIMIT 10;
        ```

        Output:

        ```sh
        +------+------------------------------------------------------+-------------+
        | id   | title                                                | releaseDate |
        +------+------------------------------------------------------+-------------+
        |    1 | Toy Story (1995)                                     | 1995-01-01  |
        |    2 | GoldenEye (1995)                                     | 1995-01-01  |
        |    3 | Four Rooms (1995)                                    | 1995-01-01  |
        |    4 | Get Shorty (1995)                                    | 1995-01-01  |
        |    5 | Copycat (1995)                                       | 1995-01-01  |
        |    6 | Shanghai Triad (Yao a yao yao dao waipo qiao) (1995) | 1995-01-01  |
        |    7 | Twelve Monkeys (1995)                                | 1995-01-01  |
        |    8 | Babe (1995)                                          | 1995-01-01  |
        |    9 | Dead Man Walking (1995)                              | 1995-01-01  |
        |   10 | Richard III (1995)                                   | 1996-01-22  |
        +------+------------------------------------------------------+-------------+
        10 rows in set (0.00 sec)
        ```
