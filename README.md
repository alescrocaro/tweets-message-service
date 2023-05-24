# tweets-message-service
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

Then you can unzip the used database
```bash
unzip tweets.csv.zip
```



## Libraries
- [RabbitMQ](https://www.rabbitmq.com/)
    - Provides advanced Message Queuing Protocol (AMQP), here we use it to build message queues, and a publish-subscriber application.

- [Pika](https://pika.readthedocs.io/en/stable/intro.html)
    - Python client for `RabbitMQ`. We will use it to create a connection with `RabbitMQ` and publish tweets to queues.

