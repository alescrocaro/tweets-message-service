# tweets-message-service
You must unzip tweets.csv

## How to run
### RabbitMQ
First you will need to [download and install](https://www.rabbitmq.com/download.html) it.



## Libraries
- [RabbitMQ](https://www.rabbitmq.com/)
    - Provides advanced Message Queuing Protocol (AMQP), here we use it to build message queues, and a publish-subscriber application.

- [Pika](https://pika.readthedocs.io/en/stable/intro.html)
    - Python client for `RabbitMQ`. We will use it to create a connection with `RabbitMQ` and publish tweets to queues.

