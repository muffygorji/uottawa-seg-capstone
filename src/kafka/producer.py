import sys
import time
import json
import pandas as pd
from kafka import KafkaProducer
import logging
import os

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

logging.basicConfig(filename=f'{os.path.expanduser("~")}/logs/build.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


def send_to_kafka(urls):
    """
    Sends the url to the given kafka topic.

    Arguments:
    url: string

    Returns: None
    """
    logger = logging.getLogger(__name__)
    producer = KafkaProducer(bootstrap_servers=config['kafka']['bootstrap_servers'],
                             api_version=tuple(config['kafka']['api_version'])
                             )

    logger.info("Sending urls to Kafka...")
    start = time.time()
    for url in urls:
        producer.send(config['kafka']['producer']['kafka_topic'], bytes(url, 'utf-8'))

    logger.info("Finished sending " + str(len(urls)) + " urls to kafka.")
    end = time.time()
    logger.info("Ellapsed time: " + str(end - start) + " for sending urls to kafka topic")


def url_bulk_load():
    """
    Sends the urls in the local csv to the given kafka topic.

    Returns: None
    """
    logger = logging.getLogger(__name__)
    bulk_load_file = pd.read_csv(config['kafka']['producer']['bulk_load_file_path'])

    try:
        if "url" not in bulk_load_file.columns:
            raise KeyError("Cannot process. Please provide a CSV file with a url column to read.")
        send_to_kafka(bulk_load_file["url"])

    except KeyError:
        logger.error("Cannot process. Please provide a CSV file with a url column to read.")



def runProducer():
    logger = logging.getLogger(__name__)
    if config['kafka']['producer']['kafka_topic'] is None:
        logger.error("Cannot process. Please make sure the kafka topic is set in the configuration file, config.py")
        exit

    else:
        url_bulk_load()


if __name__ == "__main__":
    runProducer()
