# Realtime Crypto
## Overview
This project is a data pipeline that ingests cryptocurrency data from the [Finnhub](https://finnhub.io/) API, processes it using [Kafka](https://kafka.apache.org/), stores it in [InfluxDB](https://www.influxdata.com/), and visualizes it in [Grafana](https://grafana.com/). The pipeline is orchestrated using a Makefile that simplifies the process of running various components of the system.

## Prerequisites
Before you begin, ensure that you have the following installed:

* Apache Kafka (and Zookeeper)
* InfluxDB
* Grafana
* Python 3.11 (with conda for environment management)


## Setting Up the Environment

* Create a Conda Environment:

The required Python libraries are listed in the environment.yml file. To create the environment, run:
```bash
conda create --name realtime-crypto --file environment.yml
```

* Activate the environment:
```bash
conda activate realtime-crypto
```

* Setup Environment Variables:

Create a .env file in the root directory of the project and add the following environment variables:
```plaintext
finnhub_api_key=<Your Finnhub API Key>
INFLUXDB_TOKEN=<Your InfluxDB Token>
INFLUXDB_URL=<Your InfluxDB URL> # http://localhost:8086
```

## Data Source
The data source for this project is cryptocurrency data from the [Finnhub](https://finnhub.io/) API. The data includes real-time prices and volumes for various cryptocurrency pairs, which are ingested into the pipeline via Kafka.

## Paths
The Makefile contains commands to start Zookeeper, Kafka, InfluxDB, Grafana, and the associated Python scripts for the Kafka producer and consumer.

```
Kafka Directory: F:/kafka
Grafana Directory: F:/Grafana/grafana/bin
Producer Script: src/producer.py
Consumer Script: src/consumer.py
```


## Getting Started

1. Run the following command to start the Zookeeper service:
```bash
make run-zookeeper
```

2. After Zookeeper is running, start the Kafka broker service:
```bash
make run-kafka
```

3. Run the following command to start the InfluxDB service:
```bash
make run-db
```

4. Once InfluxDB is running, start the Grafana server:
```bash
make run-grafana
```

5. Use the following command to run the Python script that fetches data from Finnhub API and produces messages to
```bash
make run-producer
```

6. Finally, run the Kafka consumer script to receive messages from the Kafka topic and store them in InfluxDB:
```bash
make run-consumer
```

## Visualization with Grafana
![Visualization](/src/image.png "Visualization")
Once all services are running, you can visualize the cryptocurrency data in Grafana.
Access Grafana by navigating to http://localhost:3000 in your browser.
Use the credentials (default: admin/admin) to log in, and configure your data source to point to the InfluxDB instance.

Create dashboards to visualize real-time cryptocurrency data.

## Notes
Ensure all paths in the Makefile are correct and match your system's configuration.
Adjust the time ranges in Grafana according to the data being collected.
Make sure that your .env file is correctly set up with your API keys and InfluxDB credentials.

