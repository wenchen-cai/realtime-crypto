"""
The main function of this project.
Get Realtime crypto maket data from finnhub
"""
import logging
import json
import os
import websocket

from dotenv import load_dotenv
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def on_message(ws: websocket.WebSocketApp, message: bytes): #pylint: disable=W0613, W0621
    """
    Load data and send to kafka
    """
    for data in json.loads(message)['data']:
        log = {"timestamp": data['t'], "symbol": data['s'], "price": data['p'], "volume": data['v']}
        producer.send("BTCUSDT", str.encode(json.dumps(log), encoding='utf-8'))
        producer.flush()


def on_error(ws: websocket.WebSocketApp, error: str): #pylint: disable=W0613, W0621
    """
    Print the errror log when scoket fail
    """
    logging.error(error)

def on_close(ws: websocket.WebSocketApp): #pylint: disable=W0613, W0621
    """
    Print the log when scoket closed
    """
    logging.info("### closed ###")

def on_open(ws: websocket.WebSocketApp): #pylint: disable=W0613, W0621
    """
    Send subsribe to the websocket
    """
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

if __name__ == "__main__":
    load_dotenv()
    finnhub_api_key = os.getenv('finnhub_api_key')
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={finnhub_api_key}",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
