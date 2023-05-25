"""
    Consume tweets from topics the user wants and create a timeline.

    Author: Alexandre Aparecido Scrocaro Junior, Pedro Klayn
    Dates: 
        start: 24/05/2023
        more info: https://github.com/alescrocaro/tweets-message-service

"""

import pika
import json
import sys
from time import sleep
from random import choice

print("> Timeline")

def callback(_, method, properties, body):
    """Function to be executed when subscriber receives a tweet. It display the tweet in timeline.

    Args:
        ch (_): _
        method (_): _
        properties (_): _
        body (string | bytes): stringified tweet
    """
    tweet = json.loads(body)


    print(tweet["user_name"] + ":")
    print(tweet["text"])
    print()
    print("------------------------------------------------------------------")
    print()


    sleep(1)




"""
    Get one tweet from a random queue the user is subscribed, to simulate a timeline
"""
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
