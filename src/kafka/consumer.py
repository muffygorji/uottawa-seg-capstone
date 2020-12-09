import sys
import time
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from src.models.predict_model import predict_model
import logging
import os

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

logging.basicConfig(filename=f'{os.path.expanduser("~")}/logs/build.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def send_to_kafka(result):
    """
    sends the url to the given kafka topic.

    Arguments:
    result: list

    Returns: None
    """
    logger = logging.getLogger(__name__)
    producer = KafkaProducer(bootstrap_servers=config['kafka']['bootstrap_servers'],
                             api_version=tuple(config['kafka']['api_version'])
                             )
    logger.info("Sending url to Kafka...")
    producer.send(config['kafka']['consumer']['kafka_topic_to_send_to'], json.dumps(result).encode('utf-8'))


def url_bulk_consume():
    """
    Consumes urls from configured kafka topic , runs the predictions on them,
    sends the malicious urls to the second configured kafka topic

    Returns: None
    """
    logger = logging.getLogger(__name__)
    consumer = KafkaConsumer(config['kafka']['consumer']['kafka_topic_to_read_from'],
                             bootstrap_servers=config['kafka']['bootstrap_servers'],
                             api_version=tuple(config['kafka']['api_version']),
                             group_id=config['kafka']['consumer']['group_id'],
                             enable_auto_commit=config['kafka']['consumer']['enable_auto_commit'],
                             auto_offset_reset=config['kafka']['consumer']['auto_offset_reset'],
                             consumer_timeout_ms=config['kafka']['consumer']['consumer_timeout_ms'],
                             max_poll_interval_ms=config['kafka']['consumer']['max_poll_interval_ms']
                             )
    start = time.time()
    logger.info("Reading data ...")
    for message in consumer:
        url = message.value.decode("utf-8")
        logger.info(url)
        result = predict_model(url)
        prediction_score = result['prediction_score']
        confidence_score = result['confidence_score']

        logger.info("prediction: " + str(prediction_score))

        if (prediction_score == config['kafka']['predicted_label'] and
                confidence_score >= config['kafka']['confidence_score']):
            logger.info("Found malicious url")
            send_to_kafka(result)
        consumer.commit()
    end = time.time()
    logger.info("Ellapsed time: " + str(end - start) + " for consuming and predicting urls from kafka topic")


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    if (config['kafka']['consumer']['kafka_topic_to_read_from'] is None or
            config['kafka']['consumer']['kafka_topic_to_send_to'] is None):
        logger.critical("Cannot process. Please make sure the kafka topics are set in the configuration file, "
                        "config.py")
        raise ValueError("Cannot process. Please make sure the kafka topics are set in the configuration file, "
                         "config.py")

    url_bulk_consume()
