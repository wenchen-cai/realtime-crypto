# Makefile

# Paths to Kafka, Grafana ,and Python scripts
KAFKA_DIR = F:/kafka
GRAFANA_DIR = F:/Grafana/grafana/bin
PRODUCER_SCRIPT = src/producer.py
CONSUMER_SCRIPT = src/consumer.py

# Commands to run Zookeeper and Kafka
run-zookeeper:
	@echo "Starting Zookeeper..."
	@$(KAFKA_DIR)/bin/windows/zookeeper-server-start.bat $(KAFKA_DIR)/config/zookeeper.properties

run-kafka:
	@echo "Starting Kafka..."
	@$(KAFKA_DIR)/bin/windows/kafka-server-start.bat $(KAFKA_DIR)/config/server.properties

# Commands to run Python scripts
run-producer:
	@echo "Running Kafka Producer..."
	@python $(PRODUCER_SCRIPT)

run-consumer:
	@echo "Running Kafka Consumer..."
	@python $(CONSUMER_SCRIPT)

# Commands to run InfluxDB and Grafana
run-db:
	@echo "Running InfluxDB..."
	@influxd

run-grafana:
	@echo "Running Grafana..."
	@cd $(GRAFANA_DIR) && ./grafana-server.exe