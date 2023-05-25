import pika
import json

all_tweets = []
published_in_topic = False

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue="tweets")

def callback(ch, method, properties, body):
    print(" [x] Received tweets")
    all_tweets = json.loads(body)

    ch.exchange_declare(exchange="tweets", exchange_type="topic")

    try:
        print(" [*] Publishing tweets in specific queues according to topic")
        for tweet in all_tweets:
            if ("realmadrid" in tweet["topic"]):
                ch.basic_publish(exchange="tweets", routing_key=tweet["topic"], body=json.dumps(tweet))
                published_in_topic = True
            if ("barcelona" in tweet["topic"] or "barca" in tweet["topic"]):
                ch.basic_publish(exchange="tweets", routing_key="barcelona", body=json.dumps(tweet))
                published_in_topic = True

        if (published_in_topic):
            print(" [x] Published tweets in queues")

    except Exception as e:
        print(f"Error while publishing tweets: {e}")

def consume_existing_tweets():
    """_summary_
    """
    # get amount of tweets in queue
    queue_info = channel.queue_declare(queue="tweets", passive=True)
    tweets_count = queue_info.method.message_count

    if tweets_count > 0:
        print(f" [*] Consuming existing {tweets_count} messages in the queue")
        channel.basic_consume(queue="tweets", on_message_callback=callback, auto_ack=True)

        # start tweets consuming
        channel.start_consuming()
    else:
        print(" [x] No existing messages in the queue")

consume_existing_tweets()
