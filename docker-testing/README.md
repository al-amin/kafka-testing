# Installing kafka and zookeeper using docker

## To know ip address in mac
```ipconfig getifaddr en0```
i.e-> 192.168.0.187

## zookeeper
From Terminal run the following to create a zookeeper docker image
```docker run -d --name zookeeper -p 2181:2181 --restart=unless-stopped wurstmeister/zookeeper```

## kafka
From Terminal run the following to create a kafka docker image
```docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=YOUR_IP_ADDRESS -e KAFKA_ZOOKEEPER_CONNECT=YOUR_IP_ADDRESS:2181 --restart=unless-stopped wurstmeister/kafka```
In my case (from Macbook Pro)-> i.e-> ```docker run -d --name kafka -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=192.168.0.187 -e KAFKA_ZOOKEEPER_CONNECT=192.168.0.187:2181 --restart=unless-stopped wurstmeister/kafka```

### Check if docker was successful
```docker -ps```

### Connect to kafka bash
From terminal run the followings
```docker exec -it kafka /bin/bash```
```cd opt/kafka/bin```
```kafka-topics.sh --create --topic TOPIC_NAME --zookeeper YOUR_IP_ADDRESS:2181 --partitions 3 --replication-factor 1```
In my case (from Macbook Pro)-> i.e-> ```kafka-topics.sh --create --topic first_topic --zookeeper 192.168.0.187:2181 --partitions 3 --replication-factor 1```
