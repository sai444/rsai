# import requests
# import json
# import kafka
# consumer = kafka.KafkaConsumer(group_id='test', bootstrap_servers=['localhost:9092'])
# st = consumer.topics()

# print(consumer.topics())




# url = "http://localhost:5000/projecttopic"




# for x in st : 
#     print(x)
#     y = x.split('_')
   
#     if (y[0]):
#       payload = json.dumps({
#         "topic":x,
#         "project": (y[1])
#       })
#       headers = {
#         'Content-Type': 'application/json'
#       }



#     response = requests.request("POST", url, headers=headers, data=payload)

#     print(response.text)


import requests
import json

url = "http://localhost:5000/projecttopic/1"

payload = json.dumps({
  "topic": "sai",
  "project": "saiproject"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
