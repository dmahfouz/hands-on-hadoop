# Section 02: Using Hadoop's Core: HDFS and MapReduce

## Installing Python, MRJob and nano

### Install Python (pip)

- SSH into HDP by using:

    `ssh maria_dev@127.0.0.1 -p 2222`

- Login as root user

    `su root`

- Install Python Pip (for HDP 2.6.5)

    `yum install python-pip`

    Enter `[y]` if prompted

### Install `mrjob`

- Still in SSH for `root` user:

    `pip install mrjob==0.5.1`

### Install `nano`

`yum install nano`