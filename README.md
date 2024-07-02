# BEES Data Engineering – Breweries Case

## Objective
The goal of this project is to demonstrate my ability to consume data from an API, transform it, and persist it into a data lake following the medallion architecture with three layers: raw data, curated data partitioned by location, and an analytical aggregated layer.

## Instructions
1. **API**: Use the [Open Brewery DB API](https://api.openbrewerydb.org/breweries) to fetch data about breweries.
2. **Orchestration Tool**: The pipeline is built using Apache Airflow to handle scheduling, retries, and error handling.
3. **Language**: The project is implemented in Python. Test cases are included to ensure the code works as expected.
4. **Containerization**: Docker is used to modularize and run the application.
5. **Data Lake Architecture**:
    - **Bronze Layer**: Raw data is persisted from the API in its native format.
    - **Silver Layer**: Data is transformed into a columnar storage format (parquet) and partitioned by brewery location.
    - **Gold Layer**: An aggregated view is created with the quantity of breweries per type and location.

## Project Structure
AB_InBev/
│
├── dags/
│ ├── brewery_pipeline.py
│
├── scripts/
│ ├── fetch_data.py
│ ├── transform_data.py
│ ├── aggregate_data.py
│
├── data/
│ ├── bronze/
│ ├── silver/
│ ├── gold/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


## Setup and Running the Project

### Prerequisites
- Docker
- Docker Compose
- AWS account with access to S3

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ste-aina/brewery-data.git
    cd AB_InBev
    ```

2. Create a `.env` file in the root of the project with the following content:
    ```plaintext
    AWS_ACCESS_KEY_ID='your_aws_access_key_id'
    AWS_SECRET_ACCESS_KEY='your_aws_secret_access_key'
    ```

3. Build and start the containers:
    ```sh
    docker-compose up --build
    ```

4. Access the Airflow web interface at `http://localhost:8080` and trigger the `brewery_pipeline` DAG.

### Configuration
Ensure your AWS credentials are correctly set up in the `.env` file. Do not commit these credentials to the repository.

## Monitoring and Alerting
To implement monitoring and alerting:
- Use Airflow's built-in logging and email alerting features.
- Set up alerts for task failures and data quality issues.
- Monitor the S3 bucket for data consistency and completeness.

## Repository Structure and Design Choices
- **DAGs**: The `brewery_pipeline.py` file defines the Airflow DAG and tasks for fetching, transforming, and aggregating the data.
- **Scripts**: Individual Python scripts for each step in the data pipeline.
- **Docker**: Dockerfile and docker-compose.yml are used for containerization and orchestration.

## Conclusion
This project demonstrates the ability to build a robust data pipeline using Airflow, Docker, and AWS S3, following best practices for data engineering.

---

Feel free to reach out if you have any questions or need further assistance.
