import kafka
consumer = kafka.KafkaConsumer(group_id='test', bootstrap_servers=['localhost:9092'])
st = consumer.topics()

print(consumer.topics())

for x in st : 
    print(x)