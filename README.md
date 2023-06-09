# kafka-testing

# [how-to-install-homebrew-on-Macbook-M1](https://www.igeeksblog.com/how-to-install-homebrew-on-mac/)

# Install java 11 using brew
```brew install java11```  [Reference link](https://medium.com/@kirebyte/using-homebrew-to-install-java-jdk11-on-macos-2021-4a90aa276f1c)

# Install python packages
Install virtual env from [link](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) \
And then install all the required packages using the following \
```pip install -r requirements.txt```

# Installing kafka and zookeeper using docker

## To know ip address in mac
```ipconfig getifaddr en0```
i.e-> 192.168.0.187

## zookeeper
From Terminal run the following to create a zookeeper docker image

```docker run -d --name zookeeper -p 2181:2181 --restart=unless-stopped wurstmeister/zookeeper```

# Installing kafka manager from CMAK
Just follow the steps from [here GitHub](https://github.com/yahoo/CMAK) or [This directory](https://github.com/al-amin/kafka-testing/tree/main/CMAK-master) \
1. ```cd CMAK-master```
2. ```./sbt clean dist```
3. ```cd target```
4. ```cd universal```
5. ```unzip cmak-3.0.0.7.zip```
6. Change the configuration in application.conf using  ```nano conf/application.conf```
7. Then change to ```cmak.zkhosts="127.0.0.1:2181"``` or localhost
8. Start the server using ```bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080```
9.  - if you face issues (Yikes! KeeperErrorCode = Unimplemented) 
10.  - then solve it by this [stackoverflow](https://stackoverflow.com/questions/67485503/keepererrorcode-unimplemented-for-kafka-manager-mutex)


#### Now create a topic with 2 partitions - after visiting localhost:8080 -> topics-> create


## kafka
From Terminal run the following to create a kafka docker image

```docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=YOUR_IP_ADDRESS -e KAFKA_ZOOKEEPER_CONNECT=YOUR_IP_ADDRESS:2181 --restart=unless-stopped wurstmeister/kafka```

In my case (from Macbook Pro)-> \
i.e-> ```docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=192.168.0.187 -e KAFKA_ZOOKEEPER_CONNECT=192.168.0.187:2181 --restart=unless-stopped wurstmeister/kafka```

### Check if docker was successful
```docker -ps```

## Connect to kafka bash

From terminal run the followings, here ```kafka``` is docker container name

```docker exec -it kafka /bin/bash```

```cd opt/kafka/bin```

```kafka-topics.sh --create --topic TOPIC_NAME --zookeeper YOUR_IP_ADDRESS:2181 --partitions 3 --replication-factor 1```

In my case (from Macbook Pro)-> \
i.e-> ```kafka-topics.sh --create --topic first_topic --zookeeper 192.168.0.187:2181 --partitions 3 --replication-factor 1```

#### To check or list the topics:
```kafka-topics.sh --zookeeper YOUR_IP_ADDRESS:2181 --list```\
```kafka-topics.sh --zookeeper 192.168.0.187:2181 --list``` 
#### To check the details of a topic:
```kafka-topics.sh --zookeeper 192.168.0.187:2181 --topic first_topic --describe``` (YOUR_IP_ADDRESS)
#### Delete a topic
```kafka-topics.sh --zookeeper YOUR_IP_ADDRESS:2181 --topic TOPIC_NAME --delete```\
```kafka-topics.sh --zookeeper 192.168.0.187:2181 --topic second_topic --delete```
## Kafka producer CLI - creating a producer
```kafka-console-producer.sh --broker-list YOUR_IP_ADDRESS:9092 --topic TOPIC_NAME```\
```kafka-console-producer.sh --broker-list 192.168.0.187:9092 --topic first_topic```
#### Now add acks property by
```kafka-console-producer.sh --broker-list 192.168.0.187:9092 --topic first_topic --producer-property acks=all```

## Kafka consumer CLI - creating a consumer
```kafka-console-consumer.sh --bootstrap-server 192.168.0.187:9092 --topic first_topic``` - its only from point in time\
```kafka-console-consumer.sh --bootstrap-server 192.168.0.187:9092 --topic first_topic --from-beginning``` - its all way from the beginning ;)

## Kafka consumer CLI - creating a consumers in groups
```kafka-console-consumer.sh --bootstrap-server 192.168.0.187:9092 --topic first_topic --group my-first-application``` - now if the producer send message, all of the consumers on this group will receive the message based on the partitions \
```kafka-console-consumer.sh --bootstrap-server 192.168.0.187:9092 --topic first_topic --group my-second-application --from-beginning``` - it will read all way from the beginning

## Kafka consumers groups CLI - managing consumers groups
```kafka-consumer-groups.sh --bootstrap-server 192.168.0.187:9092 --list``` - It will show all the consumers gourps (**NOTE**: By default when a consumer is being created, one random group also created)\
```kafka-consumer-groups.sh --bootstrap-server 192.168.0.187:9092 --describe --group my-second-application``` - It will show details of the ```my-second-application``` group

## Kafka consumers groups CLI - resetting offsets
```kafka-consumer-groups.sh --bootstrap-server 192.168.0.187:9092 --group my-second-applicatoin --reset-offsets --to-earliest --execute --topic first_topic``` - will reset from earliest/beginning\
```kafka-consumer-groups.sh --bootstrap-server 192.168.0.187:9092 --group my-second-applicatoin --reset-offsets  --shift-by -2  --execute --topic first_topic``` - will reset the offset by shifting -2 positions

## Docker STOP container
To check -> ```docker ps```\
```docker stop my_container```\
In our case -> ```docker stop kafka```\
In our case -> ```docker stop zookeeper```

## Docker START container
To check -> ```docker ps```\
```docker start my_container```\
In our case -> ```docker start kafka```\
In our case -> ```docker start zookeeper```


