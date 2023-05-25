# tweets-message-service

Project developed for distributed systems classes. The main idea is to collect tweets, insert into a queue, classify into topics and create a queue for each topic, then an client (subscriber) can watch any topic he wants.

Authors:
\
Alexandre Aparecido Scrocaro Junior
\
Pedro Klayn


## How to run

### RabbitMQ
First you will need to [download and install](https://www.rabbitmq.com/download.html) it.\
Here is an example:
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install erlang # dependency package
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl status rabbitmq-server
```

```bash
pip install -r requirements.txt
```

Then you can unzip the used database
```bash
unzip tweets.csv.zip
```

To list all existing queues:
```bash
sudo rabbitmqctl list_queues
```

To clear all existing queues (BE CAREFUL!):
```bash
sudo rabbitmqctl list_queues | awk '{print $1}' | xargs -I % sudo rabbitmqctl delete_queue %
```

To consume all tweets from database:
```bash
python collector.py # this should get all tweets and insert into a single queue
```

To split tweets into topics:
```bash
python classifier.py
```

To start a client:
```bash
python subscriber.py barcelona ajax bayern
python subscriber.py realmadrid
```

This is the common flux, but you should be able to run it in any order.


## Libraries
- [RabbitMQ](https://www.rabbitmq.com/)
    - Provides advanced Message Queuing Protocol (AMQP), here we use it to build message queues, and a publish-subscriber application.

- [Pika](https://pika.readthedocs.io/en/stable/intro.html)
    - Python client for `RabbitMQ`. We will use it to create a connection with `RabbitMQ` and publish tweets to queues.

- csv
    - Used for reading the csv file to collect tweets

- json
    - Made operations to convert dict into string and vice versa

- time
    - We used the `sleep` function to simulate a timeline of twitter

- sys 
    - Get argv in subscriber to subscribe in queues

- random
    - Select a random queue from the subscribed queues to show in timeline

