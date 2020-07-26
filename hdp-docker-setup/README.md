# Deploying HDP Hortonworks Sandbox on Docker

## Setup

Following guide in the link below to get HDP sandbox image on Docker. (Note: requires Docker install and compute with at least 10GB RAM)

https://www.cloudera.com/tutorials/sandbox-deployment-and-install-guide/3.html#further-reading

## Docker setup

Go to Docker -> Settings, select the Advanced tab and adjust the dedicated memory to **at least 10GB of RAM**.

## HDP Deployment

### Deploy HDP Sandbox

#### Install/Deploy/Start HDP Sandbox

- Download latest scripts from [Hortonworks Data Platform (HDP) for Docker](https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html?utm_source=mktg-tutorial) and decompress **zip** file.

In the decompressed folder, you will find the shell script **docker-deploy-{version#}.sh**. From the command line (bash) run the script:

```sh
cd /path/to/script
sh docker-deploy-{HDPversion}.sh
```

>Note: You only need to run script once. It will setup and start the sandbox for you, creating the sandbox docker container in the process if necessary.

>Note: The decompressed folder has other scripts and folders. We will ignore those for now. They will be used later in advanced tutorials.

## Verify HDP Sandbox
Verfiy HDP sandbox was successfully deployed by issuing the command:

```sh
docker ps
```

## Stop HDP Sandbox

When you want to stop/shutdown your HDP sandbox, run the following commands:

```sh
docker stop sandbox-dhp
docker stop sandbox-proxy
```

## Restart HDP Sandbox

When you want to re-start your sandbox, run the following commands:

```sh
docker start sandbox-dhp
docker start sandbox-proxy
```

## Remove HDP Sandbox

A container is an instance of the Sandbox image. You must **stop** container dependencies before removing it. Issue the following commands:

```sh
docker stop sandbox-sh
docker stop sandbox-proxy
docker rm sandbox-hdp
docker rm sandbox-proxy
```

If you want to remove the HDP Sandbox image, issue the following command after stopping and removing the containers:P

```sh
docker rmi hortonworks/sandbox-hdp:{release}
```

## Access HDP Dashboard
Watch the following video below to get to the HDP Sandbox dashboard:

https://www.youtube.com/watch?v=5TJMudSNn9c&feature=youtu.be

Once HDP docker image has been set-up, go to sandbox-hdp.hortonworks.com:1080 to get to the dashboard.