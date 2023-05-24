import csv

class Collector:
    def __init__(self):
        self.tweets = []
        with open('./tweets.csv', 'r') as file:
            reader = csv.reader(file)
            
            # Skip header row
            next(reader)

            for tweet in reader:
                self.tweets.append({ "topic": tweet[6][1:].lower(), "text": tweet[13], "user_name": tweet[56] })



if __name__ == '__main__':
    collector = Collector()
    for tweet in collector.tweets:
        if ('realmadrid' in tweet["topic"].lower()):
            # print(f"tweet by {tweet["user_name"]}: ")
            print(tweet)
            print()