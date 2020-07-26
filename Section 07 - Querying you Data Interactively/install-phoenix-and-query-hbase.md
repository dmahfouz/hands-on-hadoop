# Section 07: Querying you Data interactively

## Activity: Install Phoenix and query HBase with it

1. Log in to Ambari (as admin), click HBase from services and from the service actions drop down click start to start HBase

2. SSH into HDP and login as super user `su root`

3. Install Phoenix using: `yum install phoenix`
    - Enter `[y]` if prompted

4. Change directory to:

    ```sh
    cd /usr/hdp/current/phoenix-client/
    ```

    Goto bin folder:

    ```sh
    cd bin/
    ```

5. Enable cli inteface for Phoenix by running

    ```sh
    python sqlline.py
    ```

    Which should now give the Phoenix prompt:

    `0: jdbc:phoenix:> ...`

6. Run the command `!tables` to get a list of tables. This should return just the system tables at this point

7. Create a new table - US cities and their populations:

    ```sql
    CREATE TABLE IF NOT EXISTS us_population(
        state CHAR(2) NOT NULL,
        city VARCHAR NOT NULL,
        population BIGINT
        CONSTRAINT my_pk PRIMARY KEY (state, city));
    ```

    Run `!tables` to check that `us_population` table has been created

8. Insert rows into `us_population` table:
    - **Note:** Phoenix does not have an `INSERT` command but rather an `UPSERT` command. `UPSERT` means that insert this row if it does not exist, otherwise update the contents of the existing row

    ```sql
    UPSERT INTO US_POPULATION VALUES ('NY', 'New York', 8143197);
    UPSERT INTO US_POPULATION VALUES('CA', 'Los Angeles', 3844829);
    ```

    Validate this by running

    ```sql
    SELECT * FROM US_POPULATION;
    ```

9. Try other queries such as 

    ```sql
    SELECT * FROM US_POPULATION WHERE State = 'CA';
    ```

10. Clean up (drop table) using:

    ```sql
    DROP TABLE US_POPULATION;
    ```