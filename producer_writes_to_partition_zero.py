from kafka import KafkaProducer
import json, time
from data import get_registered_user

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_partition_zero(key, all, available):
    return 0

producer = KafkaProducer(bootstrap_servers=['192.168.0.187:9092'],
                         value_serializer=json_serializer,
                         partitioner=get_partition_zero)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4)