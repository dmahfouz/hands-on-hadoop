# Section 07: Querying your Data Interactively

## Activity: Integrate Phoenix with Pig

1. SSH into HDP: `ssh maria_dev@127.0.0.1 -p 2222`, login as super user `su root`

2. Navigate to Phoenix client directory:

    ```sh
    cd /usr/hdp/current/phoenix-client/bin/
    ```

3. Execute the following to get to the Phoenix prompt:

    `python sqlline.py`

4. Create a users table that matches the same schema as the MovieLens data file format

    ```sql
    CREATE TABLE users (
        USERID INTEGER NOT NULL,
        AGE INTEGER,
        GENDER CHAR(1),
        OCCUPATION VARCHAR,
        ZIP VARCHAR
        CONSTRAINT pk PRIMARY KEY(USERID)
    );
    ```

    Run `!tables` to validate `USERS` table has been created

5. Exit out of the Phoenix shell (`!quit`) and change directory to:

    ```sh
    cd /home/maria_dev
    ```

6. If there is no directory `/home/maria_dev/ml-100k/` then do the following:

    Create a directory and cd into it

    ```sh
    mkdir ml-100k/ && cd ml-100k/
    ```

    Download the `u.user` data file:

    ```sh
    wget http://media.sundog-soft.com/hadoop/ml-100k/u.user
    ```

    Download the `phoenix.pig` script:

    ```sh
    wget http://media.sundog-soft.com/hadoop/phoenix.pig
    ```

    Confirm downloaded files using `ls`

7. Inspect the `phoenix.pig` script:

    ```sql
    -- call REGISTER command to tell pig script where to get the
    -- client libraries for Pheonix, so it can use the Java classes
    -- it needs to connect Pig to Phoenix and then to HBase
    REGISTER /usr/hdp/current/phoenix-client/phoenix-client.jar

    -- load up raw data from pipe-delimited text file
    -- and transform into a relational table called users
    users = LOAD '/user/maria_dev/ml-100k/u.user'
    USING PigStorage('|')
    AS (USERID:int, AGE:int, GENDER:chararray, OCCUPATION:chararray, ZIP:chararray);

    -- stores the users relation (created in Pig) into a HBase table called
    -- users (previously created) using the PhoenixHBaseStorage connector
    -- with the parameters hostname (actual Phoenix instance we're talking
    -- to - running on localhost) and a batch size count of 5000 (meaning
    -- commit every 5000 entries - this should be no bigger than what can be
    -- fit into memory)
    STORE users into 'hbase://users' using
        org.apache.phoenix.pig.PhoenixHBaseStorage('localhost','-batchSize 5000');

    -- only load back `userid` and oocupation` into an occupations table
    -- (relation), using the PhoenixHbaseLoader class (so we can get pig)
    -- to talk to phoenix, again specifying hostname where phoenix is running
    occupations = load 'hbase://table/users/USERID,OCCUPATION' using org.apache.phoenix.pig.PhoenixHBaseLoader('localhost');

    -- perform query by grouping occupations in occupation tbl and getting
    -- count foreach group
    grpd = GROUP occupations BY OCCUPATION;
    cnt = FOREACH grpd GENERATE group AS OCCUPATION,COUNT(occupations);
    DUMP cnt;
    ```

8. Run phoenix pig script using:

    **Update**: For HDP 2.6.5 (docker) run the following:

    `pig -x mapreduce phoenix.pig`

    instead of:

    `pig phoenix.pig`

    (this seems to be cause by Phoenix not working with Tez - used as default on HDP >=2.6.5 )

    - Remember Pig runs on top of MapReduce, so this will be kicking off a number of MapReduce jobs, of which there is some overhead in starting up
    - However once started up, the Pig script will run quite quickly, especially if paralellisation in MapReduce is being taken advantage of

9. 