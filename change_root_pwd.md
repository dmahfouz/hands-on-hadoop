# Changing root password

- In order to get admin privileges, ssh into HDP using the following:

    ```sh
    ssh maria_dev@127.0.0.1 -P 2222
    ```

- Once logged in enter the following to get super user access (`su`):

    `su root`

- When prompted enter default password `hadoop`.

- Then set new password to `$pwd` where '$pwd' is your new password.

- This will then enable access to user `root` with pwd `$pwd`.

## Setting `admin` user password for Ambari

 > **Disclaimer**: May not be official instructions from course - this was done when re-setting things up

- Go to `http://localhost:4200` to get to HDP terminal

- Login as user `maria_dev`, enter password set

- Login at super user `su` with:

    ```sh
        su root
    ```

- Enter `$pwd` for root user `su` and go to `/usr/sbin/ambari-admin-password-reset`

- Enter new password for user `admin` - you will now be able to log in as `admin` in Ambari
