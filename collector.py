import csv
import json
import pika
import sys

class Collector:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.connection.channel()
        self.tweets = []
        self.preprocess_data()


    def preprocess_data(self):
        with open("./tweets.csv", "r") as file:
            reader = csv.reader(file)
            
            # Skip header row
            next(reader)

            for tweet in reader:
                self.tweets.append({ "topic": tweet[6][1:].lower(), "text": tweet[13], "user_name": tweet[56] })


    def handle_queue(self):
        self.channel.queue_declare(queue="tweets")
        stringified_tweets = json.dumps(self.tweets)
        self.channel.basic_publish(exchange="", routing_key="tweets", body=stringified_tweets)

        # self.connection.close()


if __name__ == "__main__":
    collector = Collector()
    collector.handle_queue()