import csv
import json
import pika
from time import sleep

class Collector:
    def __init__(self):
        print("initing collector...")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.connection.channel()
        self.tweets = []
        self.preprocess_data()

    def handle_queue(self, reader):
        self.channel.queue_declare(queue="tweets", durable=True)
        for tweet in reader:
            stringified_tweet = json.dumps({ "topic": tweet[6].lower(), "text": tweet[13], "user_name": tweet[56] })
            self.channel.basic_publish(exchange="", routing_key="tweets", body=stringified_tweet)
            # print('published.')
            # sleep(.1)


    def preprocess_data(self):
        print("preprocessing tweets...")
        try:
            with open("./tweets.csv", "r") as file:
                reader = csv.reader(file)
                
                # Skip header row
                next(reader)

                self.handle_queue(reader)
        
        except Exception as e:
            print(f"Error while preprocessing tweets: {e}" )




if __name__ == "__main__":
    collector = Collector()