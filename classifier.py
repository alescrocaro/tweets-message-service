import pika
import json
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="barcelona", durable=True)
channel.queue_declare(queue="realmadrid", durable=True)
channel.queue_declare(queue="bayern", durable=True)
channel.queue_declare(queue="liverpool", durable=True)
channel.queue_declare(queue="ucl", durable=True)
channel.queue_declare(queue="ajax", durable=True)

barcelona_topics = ["barcelona", "barça", "barca", "elclasico", "elclásico"]
realmadrid_topics = ["realmadrid", "elclasico", "elclásico"]
bayern_topics = ["fcbayern", "bayern"]
liverpool_topics = ["liverpool"]
ucl_topics = ["#ucl"]
ajax_topics = ["ajax"]


def callback(ch, method, properties, body):
    print("loading...")
    tweet = json.loads(body)

    try:
        for realmadrid_topic in realmadrid_topics:
            if (realmadrid_topic in tweet["topic"]):
                print(" [*] Publishing tweet in realmadrid queue...")
                ch.basic_publish(exchange="", routing_key="realmadrid", body=json.dumps(tweet))

        for barcelona_topic in barcelona_topics:
            if (barcelona_topic in tweet["topic"]):
                print(" [*] Publishing tweet in barcelona queue...")
                ch.basic_publish(exchange="", routing_key="barcelona", body=json.dumps(tweet))

        for bayern_topic in bayern_topics:
            if (bayern_topic in tweet["topic"]):
                print(" [*] Publishing tweet in bayern queue...")
                ch.basic_publish(exchange="", routing_key="bayern", body=json.dumps(tweet))

        for liverpool_topic in liverpool_topics:
            if (liverpool_topic in tweet["topic"]):
                print(" [*] Publishing tweet in liverpool queue...")
                ch.basic_publish(exchange="", routing_key="liverpool", body=json.dumps(tweet))

        for ucl_topic in ucl_topics:
            if (ucl_topic in tweet["topic"]):
                print(" [*] Publishing tweet in ucl queue...")
                ch.basic_publish(exchange="", routing_key="ucl", body=json.dumps(tweet))

        for ajax_topic in ajax_topics:
            if (ajax_topic in tweet["topic"]):
                print(" [*] Publishing tweet in ajax queue...")
                ch.basic_publish(exchange="", routing_key="ajax", body=json.dumps(tweet))

        ch.basic_ack(delivery_tag=method.delivery_tag)  # confirm tweet was read and remove from queue

        # print('\033c', end='')
        # sleep(.01)

    except Exception as e:
        print(f"Error while publishing tweets: {e}")

print(f"Consuming messages from queue")

# Read only 1 tweet 
channel.basic_qos(prefetch_count=1) 
channel.basic_consume(queue="tweets", on_message_callback=callback, auto_ack=False)

# start tweets consuming
channel.start_consuming()
