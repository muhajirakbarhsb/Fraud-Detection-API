# Fraud-Detection-API

This is a fraud detection project API built with FastAPI, Prometheus, and Grafana. It is containerized using Docker for easy deployment and scalability.

## Features
- Provides an API for fraud detection
- Collects metrics using Prometheus
- Visualizes metrics using Grafana
- Easily deployable using Docker

## Prerequisites
Before running the project, make sure you have the following installed:

- Docker 
- Docker Compose
- Python

## Getting Started
Follow these steps to get the project up and running:

1. Clone the repository:
```bash
git clone https://github.com/muhajirakbarhsb/Fraud-Detection-API.git
```
2. **Change directory**:
```bash
cd Fraud-Detection-API
```
3. Build the Docker image:
```bash
docker-compose build
```
4. Start the services:
```bash
docker-compose up -d
```

This will start the FastAPI server, Prometheus, and Grafana in detached mode.

5. Access the API:

The API is now accessible at http://localhost:8000. You can use tools like cURL or Postman to interact with the API endpoints.

6. Access Prometheus:

Prometheus is running at http://localhost:9090. You can use this URL to configure Prometheus for scraping metrics from the API.

7. Access Grafana:

Grafana is running at http://localhost:3000. Use your web browser to access this URL and configure data sources and dashboards to visualize the collected metrics.

## Making Requests

To interact with the Fraud Detection API, you can use the provided `test.py` file. Follow the steps below to run the script:

1. Make sure you have Python installed on your system.

2. Install the required dependencies:

   ```bash
   pip install requests
   ```
3. Open the test.py file and modify the API endpoint and payload according to your needs.

4. Run the script:
  ```bash
  python test.py
  ```
The script will make a request to the API and display the response.
### Note: Ensure that the API server is running before executing the test.py script.

## Configuration
The project configuration can be modified through the following files:

- docker-compose.yml: Docker Compose configuration file for defining services and their dependencies.

- app/main.py: FastAPI application configuration file.

- config/prometheus.yml: Prometheus configuration file for specifying scraping targets and other settings.

- config/grafana_datasources.yml: Grafana configuration file for defining the Prometheus data source.

- config/grafana_dashboards.yml: Grafana configuration file for provisioning dashboards.

- dashboard/dashboard.json: Grafana dashboard layout

Feel free to modify these files according to your specific requirements.

## Monitoring
The project includes Prometheus and Grafana for monitoring and visualization. By default, metrics are exposed at the /metrics endpoint of the FastAPI server. Prometheus collects these metrics, which can then be visualized in Grafana.

To configure custom metrics or modify the existing ones, refer to the Prometheus and Grafana documentation.

## Acknowledgments
This project was inspired by the need for fraud detection in various domains. We would like to acknowledge the contributions of the open-source community and the following projects:

- FastAPI: https://fastapi.tiangolo.com/
- Prometheus: https://prometheus.io/
- Grafana: https://grafana.com/

Contact
For any questions or inquiries, please contact [muhajirakbarhsb@gmaiil.com]
