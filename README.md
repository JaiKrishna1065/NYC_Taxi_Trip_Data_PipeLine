🚕 NYC Taxi Data Engineering Pipeline
📌 Project Overview

This project implements an end-to-end Data Engineering ETL pipeline using the NYC Yellow Taxi Trip dataset to demonstrate real-world data ingestion, transformation, data modeling, and analytics.

The pipeline processes 3.4+ million taxi trip records, applies data quality checks, designs an OLAP star schema, loads the data into MySQL, and supports analytical querying and dashboarding.

🏗️ Architecture
NYC Taxi Parquet Files
        ↓
Python ETL (Pandas, PyArrow)
        ↓
Data Cleaning & Transformation
        ↓
Star Schema (Fact & Dimensions)
        ↓
MySQL (OLAP Database)
        ↓
Analytics SQL Queries

📊 Dataset

Source: NYC Yellow Taxi Trip Data

Format: Parquet

Volume: ~3.4 million records (January 2025)

Key Attributes: pickup time, dropoff time, trip distance, fare amount, payment type, locations

🧠 Data Modeling (Star Schema)
⭐ Fact Table

fact_nyc_taxi_data

trip_distance

fare_amount

tip_amount

total_amount

passenger_count

trip_duration_sec

date_id (FK)

payment_id (FK)

pickup_location_id

dropoff_location_id

⭐ Dimension Tables

dim_date – date, day, month, year, weekday/weekend

dim_location – pickup & dropoff location IDs

dim_payment – payment types

This structure enables fast, scalable analytical queries.

🔁 ETL Pipeline Steps
1️⃣ Extract

Read large Parquet files using PyArrow

Convert to Pandas DataFrame

Persist raw data for traceability

2️⃣ Transform

Type casting with errors='coerce'

Data quality filtering (invalid fares, distances, timestamps)

Feature engineering (trip duration, date attributes)

Column standardization

3️⃣ Load

Chunk-based bulk inserts using SQLAlchemy

Load dimension tables first

Map surrogate keys (date_id)

Load fact table

Supports safe reprocessing

⚙️ Technologies Used

Python

Pandas

PyArrow

SQLAlchemy

MySQL

SQL

Git & GitHub

📈 Analytics Use Cases

Daily and monthly revenue trends

Weekday vs weekend trip analysis

Payment method distribution

High-demand pickup/dropoff locations

Average trip distance and fare analysis

🚀 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/JaiKrishna1065/NYC_Taxi_Trip_Data_PipeLine.git
cd NYC_Taxi_Trip_Data_PipeLine

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Database

Create db_config.py using sample values:

DB_URL = "mysql+mysqlconnector://username:password@localhost:3306/nyc_taxi"

4️⃣ Run ETL Pipeline
python main.py

📁 Project Structure
NYC_Taxi_Trip_Data_PipeLine/
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── db_config_sample.py
│
├── sql/
│   ├── schema.sql
│   ├── analytics_queries.sql
│
├── data/
│   ├── raw/        (ignored)
│   └── processed/ (ignored)
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

🛡️ Best Practices Implemented

Chunk-based processing for large datasets

Logging for pipeline monitoring

Star schema modeling for OLAP workloads

Idempotent and restart-safe design

Clean Git repository management

🔮 Future Enhancements

Automate pipeline using Apache Airflow

Migrate data warehouse to Snowflake

Implement incremental data loading

Add data quality validation framework

Deploy dashboards to cloud BI tools
