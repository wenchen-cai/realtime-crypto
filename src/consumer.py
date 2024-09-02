"""
Consume the data from the kafka, and insert into InfluxDB
"""
import logging
import json
import os

from dotenv import load_dotenv
from influxdb_client import InfluxDBClient
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
from kafka import KafkaConsumer


if __name__ == "__main__":
    consumer = KafkaConsumer(
        'BTCUSDT',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        group_id='my-group'
    )

    load_dotenv()
    token = os.environ.get("INFLUXDB_TOKEN")
    url = os.environ.get("INFLUXDB_URL")
    org = "none"
    bucket="realtime-crypto"
    write_client = InfluxDBClient(url=url,token=token,org=org)
    write_api = write_client.write_api(write_options=SYNCHRONOUS)


    for message in consumer:
        message = message.value.decode('utf-8')
        data = json.loads(message)

        point = (
            Point(data['symbol'])
            .tag("symbol", data['symbol'])
            .field("price", float(data['price']))
            .field("volume", float(data['volume']))
            .time(data['timestamp'] * 1000000)
        )
        write_api.write(bucket=bucket, org=org, record=point)
        logging.info("Received message: %s", message)
