# Section 07: Querying your data interactively

## Activity: Install Presto and query Hive with it

### Agenda

- Set up Presto
- Query our Hive ratings table using Presto
- Spin Cassandra (back) up, and query our users table in Cassandra with Presto
- Execute a query that joins users in Casandra with ratings in Hive

### Install Presto

1. SSH into HDP and login as super user using `su root`


2. Goto prestodb.io/docs/current/installation/deployment.html and copy `presto-server-0234.tar.gz` link address and enter the following in the ssh terminal:

    --update (2020-05-11): **do not use** presto-server v0.234.X, use v0.228 instead**

    ```sh
    wget https://repo1.maven.org/maven2/com/facebook/presto/presto-server/0.228/presto-server-0.228.tar.gz
    ```

    **Note**: in a production setting  you would download this into a public and more permanent share that other users would have access to

3. Decompress the tarball file using:

    ```sh
    tar -xvf presto-server-0.234.tar.gz
    ```

4. `cd` into new Presto directory

    ```sh
    cd presto-server-0.234
    ```

    Where all scripts can be found for Presto in the `bin/` folder

    **Note:** Presto does not provide any configuration files at all, these need to be done when Presto is installed

5. Download configuration files using:

    ```sh
    wget http://media.sundog-soft.com/hadoop/presto-hdp-config.tgz
    ```

    And decompress using

    ```sh
    tar -xvf presto-hdp-config.tgz
    ```

    To create a `/etc/` folder with all config files

    

6. Copy link address for the Presto cli interface from https://prestodb.io/docs/current/installation/cli.html and download as follows:

    **--update (2020-05-11): again do not use presto-cli v0.234.X, use v0.228 instead**


    `cd` to `bin/` directory

    ```sh
    cd presto-server/bin/
    ```

    Download the tarball using:

    ```sh
    wget https://repo1.maven.org/maven2/com/facebook/presto/presto-cli/0.228/presto-cli-0.228-executable.jar
    ```

    Then rename using:

    ```sh
    mv presto-cli-0.234.2-executable.jar presto
    ```

7. Make the file executable using the following:

    ```sh
    chmod +x presto
    ```

8. Go to presto-server-x.x.x directory and run

    ```sh
    cd presto-server-0.234
    ```

    And start using the following command:

    ```sh
    bin/launcher start
    ```

    Go to Presto dashboard on:

    `http://127.0.0.1:8090/ui/`

9. Connect using cli interface using:

    ```sh
    bin/presto --server 127.0.0.1:8090 --catalog hive
    ```

    To view all schemas:

    ```sql
    show schemas;
    ```

    View all tables in a schema:

    ```sql
    show tables from movielens;
    ```

    Run queries

    ```sql
    select * from movielens.ratings where rating = 5;
    ```

    ```sql
    select count(*) from movielens.ratings where rating = 1;
    ```

    etc..

10. Exit shell using `quit`

11. Clean up: stop Presto service using `bin/launcher stop`