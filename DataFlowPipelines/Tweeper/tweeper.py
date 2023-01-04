from faker import Faker
from google.cloud import pubsub_v1

import random
import json
import datetime
import time

PROJECT_ID = 'awesome-treat-369215'
TOPIC = 'tweeps'

usernames = []
faker = Faker()
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID,TOPIC)

def publish(publisher,topic,message):
    data = message.encode('utf-8')
    return publisher.publish(topic_path,data=data)

def generate_tweep():
    data={}
    data['created_at'] = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S')
    data['tweep_id'] = faker.uuid4()
    data['text'] = faker.sentence()
    data['user'] = random.choice(usernames)
    print(json.dumps(data))
    return json.dumps(data)


if __name__=="__main__":
    for i in range(200):
        newprofile = faker.simple_profile()
        usernames.append(newprofile['username'])
    print("Ctrl+C to stop tweeping")
    while True:
        publish(publisher,topic_path,generate_tweep())
        time.sleep(0.5)
