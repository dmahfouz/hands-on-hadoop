# Section 06: Using non-relational data stored with Hadoop

## HBase / Pig integration - populating HBase at scale

### Limitations of importing data to HBase using Python (via REST)

- Using Python to import data to HBase via the HBase rest service is useful but not well suited for big data
- E.g.: If the size of the data is too large to fit or be read into memory on local machine it is being imported from
- Pig however is designed to efficiently move large data from a HDFS cluster to HBase

### Integrating Pig with HBase

- Must create HBase table ahead of time :white_check_mark:
- You relation must have a unique key as its first column, followed by subsequent columns as you want them saved in HBase :white_check_mark:
- `USING` clause allows you to STORE into an HBase table :white_check_mark:
- Can work at scale - HBase is transactional on rows :white_check_mark:

### Steps

1. Go to Ambari, add the relevant data files (`u.item`, `u.data`, `u.user`) into the directory `/home/user/maria_dev/ml-100k`

2. SSH into HDP and type `hbase shell` to access the HBase shell

3. Create a new table `users` consisting of the column family `userinfo`

    ```hbase
    create 'users','userinfo'
    ```

4. Download/create `hbase.pig` script as follows:

    ```sql
    users = LOAD '/user/maria_dev/ml-100k/u.user'
    USING PigStorage('|')
    AS (userID:int, age:int, gender:chararray, occupation:chararry, zip:int);

    STORE users INTO 'hbase://users'
    -- first column 'userID' is the key
    -- all other columns are stored as type `<column-family>:<column>`
    USING org.apache.pig.backend.hadoop.hbase.HBaseStorage (
        'userinfo:age,userinfo:gender,userinfo:occupation,userinfo:zip`';
    )
    ```

5. Run using `pig hbase.pig`

6. Go back to hbase shell using `hbase shell`

    - List tables using `list`
    - Use scan command to see what is in tables: `scan 'users'`

### Clean up

7. In Hbase shell, disable table first (before dropping) using `disable 'users'`

8. Drop table using: `drop 'users'`

9. Performing a `list` command in the Hbase shell should show `users` table is no longer there
