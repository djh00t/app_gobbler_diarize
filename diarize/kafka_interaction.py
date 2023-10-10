from kafka import KafkaConsumer, KafkaProducer

def setup_kafka_consumer(broker_address, topic_name):
    """Setup and return a Kafka consumer."""
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=[broker_address]
    )
    return consumer

def setup_kafka_producer(broker_address):
    """Setup and return a Kafka producer."""
    producer = KafkaProducer(bootstrap_servers=[broker_address])
    return producer

def consume_messages(consumer):
    """Consume and return messages from a Kafka topic."""
    for message in consumer:
        yield message.value

def publish_message(producer, topic_name, message):
    """Publish a message to a Kafka topic."""
    producer.send(topic_name, value=message)
