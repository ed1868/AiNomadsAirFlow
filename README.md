# Airflow DAGs Project

This project contains Apache Airflow DAGs for various tasks, including running Python functions and uploading CSV files to S3.

## Project Structure

- **dags/**: Contains the DAG definitions.
  - `run_python_function.py`: A DAG that runs a simple Python function every minute.
- **config/**: Configuration files for Airflow.
  - `airflow.cfg`: Airflow configuration settings.
- **docker-compose.yaml**: Docker Compose file to set up the Airflow environment.
- **logs/**: Directory for Airflow logs.
- **upload_csv_to_s3.py**: Script for uploading CSV files to S3.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.6+ installed.

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up the Airflow environment:**

   Use the provided `docker-compose.yaml` to start the Airflow services.

   ```bash
   docker-compose up -d
   ```

3. **Access the Airflow web interface:**

   Open your browser and go to `http://localhost:8080`. Use the default credentials to log in.

## Usage

- **Running DAGs:**

  The DAGs are scheduled to run automatically based on their defined schedules. You can also trigger them manually from the Airflow web interface.

- **Logs:**

  Check the `logs/` directory for detailed logs of DAG runs.

## Configuration

- **Airflow Configuration:**

  Modify `config/airflow.cfg` to change Airflow settings.

- **Docker Configuration:**

  Update `docker-compose.yaml` to adjust the Docker setup.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
