# Section 05: Using relational data stores with Hadoop

## Activity: Use Sqoop to import data from MySQL to HDFS/Hive

1. Once installed and able to access mysql, enter the following in the ssh terminal to access mysql cli:

    ```sh
    mysql -uroot -phadoop
    ```

2. Create database with the following command:

    ```sql
    mysql> create database movielens;
    ```

3. Check database was created:

    ```sql
    mysql> show databases;
    ```

    Which should give the following output:

    ```shell
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | druid              |
    | hive               |
    | movielens          |
    | mysql              |
    | performance_schema |
    | ranger             |
    | superset           |
    | sys                |
    +--------------------+
    9 rows in set (0.00 sec)
    ```

4. Alternatively, download the sql script to generate the dataset:

    ```sh
    wget http://media.sundog-soft.com/hadoop/movielens.sql
    ```

5. Once downloaded sql script, log back into mysql command prompt and enter the following to allow mysql to deal with less common characters in script

    ```sql
    mysql> SET NAMES 'utf8';
    mysql> SET CHARACTER SET utf8;
    ```

6. Import data using SQL script

    ```sql
    mysql> use movielens;
    mysql> source movielens.sql
    ```

    Enter the following to view tables once operation is complete

    ```sql
    mysql> show tables;
    ```

    Which should return the following output:

    ```sh
    +---------------------+
    | Tables_in_movielens |
    +---------------------+
    | genres              |
    | genres_movies       |
    | movies              |
    | occupations         |
    | ratings             |
    | users               |
    +---------------------+
    6 rows in set (0.00 sec)
    ```

7. Querying the data

    Enter the following commands to query newly created tables

    ```sql
    select * from movies limit 10;
    ```

    Output:

    ```sh
    +----+------------------------------------------------------+--------------+
    | id | title                                                | release_date |
    +----+------------------------------------------------------+--------------+
    |  1 | Toy Story (1995)                                     | 1995-01-01   |
    |  2 | GoldenEye (1995)                                     | 1995-01-01   |
    |  3 | Four Rooms (1995)                                    | 1995-01-01   |
    |  4 | Get Shorty (1995)                                    | 1995-01-01   |
    |  5 | Copycat (1995)                                       | 1995-01-01   |
    |  6 | Shanghai Triad (Yao a yao yao dao waipo qiao) (1995) | 1995-01-01   |
    |  7 | Twelve Monkeys (1995)                                | 1995-01-01   |
    |  8 | Babe (1995)                                          | 1995-01-01   |
    |  9 | Dead Man Walking (1995)                              | 1995-01-01   |
    | 10 | Richard III (1995)                                   | 1996-01-22   |
    +----+------------------------------------------------------+--------------+
    10 rows in set (0.00 sec)
    ```

    Get table schemas:

    ```sql
    mysql> describe ratings;
    ```

    Output:

    ```sh
    +----------+-----------+------+-----+-------------------+-----------------------------+
    | Field    | Type      | Null | Key | Default           | Extra                       |
    +----------+-----------+------+-----+-------------------+-----------------------------+
    | id       | int(11)   | NO   | PRI | NULL              |                             |
    | user_id  | int(11)   | YES  |     | NULL              |                             |
    | movie_id | int(11)   | YES  |     | NULL              |                             |
    | rating   | int(11)   | YES  |     | NULL              |                             |
    | rated_at | timestamp | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
    +----------+-----------+------+-----+-------------------+-----------------------------+
    5 rows in set (0.00 sec)
    ```

    Join datasets and find most popular movies by total number of ratings

    ```sql
    mysql> SELECT movies.title, COUNT(ratings.movie_id) AS ratingCount
        -> FROM movies
        -> INNER JOIN ratings
        -> ON movies.id = ratings.movie_id
        -> GROUP BY movies.title
        -> ORDER BY ratingCount DESC
        -> LIMIT 10;
    ```

    Output:

    ```sh
    +-------------------------------+-------------+
    | title                         | ratingCount |
    +-------------------------------+-------------+
    | Star Wars (1977)              |         583 |
    | Contact (1997)                |         509 |
    | Fargo (1996)                  |         508 |
    | Return of the Jedi (1983)     |         507 |
    | Liar Liar (1997)              |         485 |
    | English Patient, The (1996)   |         481 |
    | Scream (1996)                 |         478 |
    | Toy Story (1995)              |         452 |
    | Air Force One (1997)          |         431 |
    | Independence Day (ID4) (1996) |         429 |
    +-------------------------------+-------------+
    10 rows in set (0.26 sec)
    ```
