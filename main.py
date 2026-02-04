from sympy import false
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.logger import get_logger

logger = get_logger()

FILE_PATH = "D:/Python-Learning/NYC_Taxi_Trip_PipeLine/data/raw/yellow_tripdata_2025-01.parquet"

if __name__ == "__main__":
    try:
        logger.info("ETL pipeline Started")
        raw_df = extract_data(FILE_PATH)
        raw_df.to_csv(
        "data/raw/yellow_tripdata_2025-01.csv",
        index=False,
        chunksize=100_000
        )
        clean_df = transform_data(raw_df)
        load_data(clean_df)
        logger.info("ETL PipeLine Completed")
    except Exception as e:
        logger.error(f"ETL Pipeline failed due to {e}")