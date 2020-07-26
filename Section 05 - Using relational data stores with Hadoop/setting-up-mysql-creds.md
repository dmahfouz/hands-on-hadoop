# Note for HDP 2.6.5 and later

On newer HDP sandboxes, mysql's root account has no default password. You need to set one up the hard way first. If the password 'hadoop' didn't work, enter the following commands:

```sh
su root
systemctl stop mysqld
systemctl set-environment MYSQLD_OPTS= "--skip-grant-tables --skip-networking"
systemctl start mysqld
mysql -uroot
```

Then, in the SQL shell, run:

```sql

FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'hadoop';
FLUSH PRIVILEGES;
QUIT;
```

Back at the shell, run:

```sh
systemctl unset-environment MYSQLD_OPTS
systemctl restart mysqld
exit
```

Now you should be able to successfully connect with:

```sh
mysql -uroot -phadoop
```
