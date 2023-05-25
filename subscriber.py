import pika
import json
import sys
from time import sleep
from random import choice

print("> Timeline")

def callback(ch, method, properties, body):
    tweet = json.loads(body)


    print(tweet["user_name"] + ":")
    print(tweet["text"])
    print()
    print("------------------------------------------------------------------")
    print()


    sleep(1)




connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print('queue_name: %s' % queue_name)

tweet_topics = sys.argv[1:]

while True:
    random_tweet_topic = choice(tweet_topics)

    print(f'random_tweet_topic: "{random_tweet_topic}"')
    
    # Consume a single message from the chosen queue
    method_frame, properties, body = channel.basic_get(queue=random_tweet_topic, auto_ack=False)

    # Check if a message was received
    if method_frame is not None:
        callback(None, method_frame, properties, body)
