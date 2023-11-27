# 3rd-Semester-Capstone
building a complete data pipeline

Moving San Francisco Dataset from Web to GCP with Airflow and Exploratory Analysis with dbt
This README provides detailed steps to move the San Francisco dataset from a web source to Google Cloud Platform (GCP) using Apache Airflow. The data will then be further analyzed exploratorily using dbt (data build tool).

1. Prerequisites
2. Setting Up Airflow
3. Creating Airflow DAG
4. Configuring GCP Connection in Airflow
5. Web-to-GCS Operator
6. dbt Installation and Configuration
7. Exploratory Analysis with dbt


1. Prerequisites
Google Cloud Platform (GCP) Account: Ensure you have a GCP account with the necessary permissions.
Apache Airflow: Install and configure Apache Airflow on your local machine or a server.
dbt (data build tool): Install dbt for exploratory analysis.

2. Setting Up Airflow
Follow the official Apache Airflow documentation to install and set up Airflow. 
Make sure to initialize the Airflow database.

3. Creating Airflow DAG
Create an Airflow Directed Acyclic Graph (DAG) to orchestrate the data movement process. 

4. Configuring GCP Connection in Airflow
In the Airflow web UI, navigate to Admin -> Connections and add a new connection for GCP. Enter your GCP credentials (project ID, keyfile path, etc.).

5. Web-to-GCS Operator
Implement a custom Airflow operator (WebToGCSOperator) to fetch data from the web and upload it to GCS. 

6. dbt Installation and Configuration
Install dbt using the following command:

```bash
pip install dbt ```

Create a dbt profile file (profiles.yml) with your GCP BigQuery credentials. 

7. Exploratory Analysis with dbt
Create dbt models based on your data analysis requirements.
Run dbt to execute the models and generate analysis results:

```bash
dbt run ```
Explore the generated analysis in the dbt web UI or other visualization tools.

8. Create a packages.yml file in the dbt project direcory and input the followwing
```bash
packages: 
  - package: dbt-labs/dbt_utils
    version: 1.0.0

  - package: calogica/dbt_expectations
    version: [">=0.8.0", "<0.9.0"]

  - package: dbt-labs/codegen
    version: 0.11.0```

9. Create your "staging", "intermediate" and "marts" folders in the "models" folder for your "yml" and "sql" scripts

10. For this dataset, I have a fact table and two  dimensions tables.
