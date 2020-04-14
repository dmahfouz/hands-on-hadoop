# Start HBase REST service

> **Note**: On HDP 2.6.5 Docker setup, port forwarding **does not** need to be configured. By enabling the HBase REST service via HDP SSH shell, python is able to connect from a local machine to HDP (at least tested on Windows 10 HDP 2.6.5 Docker setup)

1. SSH into HDP for user `maria_dev`:

    ```sh
    ssh maria_dev@127.0.0.1 -p 2222
    ```

2. Log in as super user (`su`)

    ```sh
    su root
    ```

    Enter `$pwd` for user `su`

3. Enable HBase REST service and info server using the following:

    ```sh
    /usr/hdp/current/hbase-master/bin/hbase-daemon.sh start rest \
        -p 8000 \
        --infoport 8001
    ```

    Where you should receive the following output when successful:

    ```console
    [root@sandbox maria_dev]# starting rest, logging to /var/log/hbase/hbase-maria_dev-rest-sandbox.hortonworks.com.out
    ```

4. To stop REST service enter the following

    ```console
    [root@sandbox maria_dev]# /usr/hdp/current/hbase-master/bin/hbase-daemon.sh stop rest
    ```
