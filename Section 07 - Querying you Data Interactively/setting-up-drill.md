# Section 07: Querying your Data interactively

## Activity: Setting up Drill

1. SSH into HDP using

    `ssh maria_dev@127.0.0.1 -P 2222`

2. Login as `root` user: `su root`

3. Download v1.12 of Apache Drill - most recent version that works with HDP (not native on HDP) using:

    `wget http://archive.apache.org/dist/drill/drill-1.12.0/apache-drill-1.12.0.tar.gz`

4. Decompress (unzip) folder using:

    `tar -xvf apache-drill-1.12.0.tar.gz`

5. Change directory to decompressed folder:

    `cd apache-drill-1.12.0/`

6. Start up servers for Apache Drill and override the default port so that it's open to the outside world and we can communicate with drill from our (local) web browser that's running the host system:

    **Update:** For HDP 2.6.5 (Docker) use:

    `bin/drillbit.sh start -Ddrill.exec.http.port=8765`

    insead of:

    `bin/drillbit.sh start -Ddrill.exec.port=8765`

    NB: This needs to be specified for Docker container (using `-Ddrill.exec.port=8765`)

7. Go to `127.0.0.1:8765` to view Drill server

8. If `Hive` and `MongoDB` are not in the enabled storage plugins list then click enable so that they then appear in the enable storage plugins list

9. Click on update button for Hive and update the configuration by adding `thrift://localhost:9083` to the `"hive.metasotre.uris"` field to give the following configuration:

    ```json
    {
        "type": "hive",
        "enabled": true,
        "configProps": {
            "hive.metastore.uris": "thrift://localhost:9083",
            "javax.jdo.option.ConnectionURL": "jdbc:derby:;databaseName=../sample-data/drill_hive_db;create=true",
            "hive.metastore.warehouse.dir": "/tmp/drill_hive_wh",
            "fs.default.name": "file:///",
            "hive.metastore.sasl.enabled": "false"
        }
    }
    ```

    Click update to continue

## Activity: Querying across multiple databases with Apache Drill

1. Once Apache Drill is set up, go to Query tab in web browser UI and enter to following to see all database tables in HDP:

    ```sql
    SHOW DATABASES;
    ```

    Which gives the results:

    | SCHEMA_NAME       |
    |-------------------|
    |INFORMATION_SCHEMA |
    |cp.default         |
    |dfs.default        |
    |dfs.root           |
    |dfs.tmp            |
    |hive.default       |
    |hive.foodmart      |
    |hive.movielens     |
    |mongo.local        |
    |mongo.movielens    |
    |sys                |

    This shows all databases prefixed with db name

2. View data from Hive `movielens` database:

    ```sql
    SELECT * FROM hive.movielens.ratings LIMIT 10;
    ```

    This should give the following results fairly quickly (given that it is translating a SQL query into an actual physical plan on Hive)

    | user_id | movie_id | rating | epoch_seconds |
    |---------|----------|--------|---------------|
    | 196     | 242      | 3      | 881250949     |  
    | 186     | 302      | 3      | 891717742     |
    | 22      | 377      | 1      | 878887116     |
    | 244     | 51       | 2      | 880606923     |
    | 166     | 346      | 1      | 886397596     |
    | 298     | 474      | 4      | 884182806     |
    | 115     | 265      | 2      | 881171488     |
    | 253     | 465      | 5      | 891628467     |
    | 305     | 451      | 3      | 886324817     |
    | 6       | 86       | 3      | 883603013     |

3. Do the same for MongoDB:

    ```sql
    SELECT * FROM mongo.movielens.users LIMIT 10;
    ```

    Note that no index has been set up for this table. This should give the following results:

    |_id         |age |gender |occupation    |user_id |zip   |
    |------------|----|-------|--------------|--------|------|
    |[B@1078c9d6 |24  |M      |technician    |1       |85711 |
    |[B@3018658f |53  |F      |other         |2       |94043 |
    |[B@283bdaa2 |23  |M      |writer        |3       |32067 |
    |[B@76761425 |24  |M      |technician    |4       |43537 |
    |[B@20165544 |33  |F      |other         |5       |15213 |
    |[B@53d178d4 |42  |M      |executive     |6       |98101 |
    |[B@254946c6 |57  |M      |administrator |7       |91344 |
    |[B@6358b976 |36  |M      |administrator |8       |05201 |
    |[B@71767c2c |29  |M      |student       |9       |01002 |
    |[B@2939ad0e |53  |M      |lawyer        |10      |90703 |

4. Write a SQL query that does a join [across databases] between data on Hive and MongoDB (or files in HDFS)

    ```sql
    SELECT
        u.occupation
        , COUNT(*)
    FROM hive.movielens.ratings r
    JOIN mongo.movielens.users u
        ON r.user_id = u.user_id
    GROUP BY u.occupation;
    ```

    Which should give the following results:

    | occupation    | EXPR$ |
    |---------------|-------|
    |none           |901    |
    |technician     |3506   |
    |retired        |1609   |
    |doctor         |540    |
    |other          |10663  |
    |healthcare     |2804   |
    |scientist      |2058   |
    |educator       |9442   |
    |artist         |2308   |
    |lawyer         |1345   |
    |programmer     |7801   |
    |engineer       |8175   |
    |librarian      |5273   |
    |homemaker      |299    |
    |administrator  |7479   |
    |student        |21957  |
    |writer         |5536   |
    |executive      |3403   |
    |marketing      |1950   |
    |entertainment  |2095   |
    |salesman       |856    |

### Clean up

Shutdown drill using:

```sh
bin/drillbit.sh stop
```

in the `/home/maria_dev/apache-drill-1.12.0/` folder.

And remember to shutdown MongoDB in Ambari UI