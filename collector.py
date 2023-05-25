"""
    Consume all tweets from tweets.csv file and insert all (one by time) in the main queue.

    Author: Alexandre Aparecido Scrocaro Junior, Pedro Klayn
    Dates: 
        start: 24/05/2023
        more info: https://github.com/alescrocaro/tweets-message-service

"""

import csv
import json
import pika
from time import sleep

class Collector:
    def __init__(self):
        """Init collector (connection, and call preprocess_data)
        """
        print("initing collector...")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.connection.channel()
        # self.tweets = []
        self.preprocess_data()

    def handle_queue(self, reader):
        """publish all tweets in tweets queue, one by time

        Args:
            reader (_reader): csv_reader, object returned when read tweets.csv containing all tweets from file
        """
        try:
            self.channel.queue_declare(queue="tweets", durable=True)
            for tweet in reader:
                stringified_tweet = json.dumps({ "topic": tweet[6].lower(), "text": tweet[13], "user_name": tweet[56] })
                self.channel.basic_publish(exchange="", routing_key="tweets", body=stringified_tweet)
                # print('published.')
                # sleep(.1)
        
        except Exception as e:
            print(f"Error while publishing tweets: {e}" )


    def preprocess_data(self):
        """Read all tweets from tweets.csv file, exclude its header and calls handle_queue to publish tweets
        """
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