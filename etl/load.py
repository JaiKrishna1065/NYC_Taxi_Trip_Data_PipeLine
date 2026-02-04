from sqlalchemy import create_engine, text
from etl.logger import get_logger
from etl.db_config import DB_URL
import pandas as pd

logger = get_logger()

# Star Schema Loading Code
def load_dim_date(df,engine):
    logger.info("Loading dim_date")
    dim_date_df = (df[['date','year','month','day','day_type']]
                    .drop_duplicates()
                    .rename(columns = {'date' : 'full_date'})
                )
    dim_date_df.to_sql('dim_date', con = engine, if_exists = 'append', index = False)

def get_date_mapping(engine):
    query = "SELECT date_id, full_date FROM dim_date"
    with engine.connect() as con:
        result = con.execute(text(query))
        rows = result.fetchall()
    return {row[1]: row[0] for row in rows}

def load_dim_location(df,engine):
    logger.info("Loading dim_location")
    dim_location_df = pd.concat(
        [
            df[['pickup_location_id']].rename(columns={'pickup_location_id':'location_id'}),
            df[['dropoff_location_id']].rename(columns={'dropoff_location_id':'location_id'})
        ]
    ).drop_duplicates()
    dim_location_df.to_sql('dim_location', con = engine, if_exists = 'append', index = False)

def load_dim_payment(df,engine):
    logger.info("Loading dim_payment")
    dim_payment_df = df[['payment_id']].drop_duplicates()
    dim_payment_df.to_sql('dim_payment', con = engine, if_exists = 'append', index = False)


def load_fact_table(df,engine,date_mapping):
    logger.info("Loading fact table")
    df['date_id'] = df['date'].map(date_mapping)
    fact_df = df[
        [
            'pickup_datetime',
            'dropoff_datetime',
            'passenger_count',
            'trip_distance',
            'fare_amount',
            'tip_amount',
            'total_amount',
            'trip_duration_sec',
            'date_id',
            'payment_id',
            'pickup_location_id',
            'dropoff_location_id'
        ]
    ]
    fact_df.to_sql(
    'fact_nyc_taxi_data',
    con=engine,
    if_exists='append',
    index=False,
    chunksize=50_000,     
    method='multi'  
)

def load_data(df):
    logger.info("Loading Data is Started")
    engine = create_engine(DB_URL)
    with engine.begin(): 
        load_dim_date(df, engine)
        load_dim_location(df, engine)
        load_dim_payment(df, engine)
        date_map = get_date_mapping(engine)
        load_fact_table(df, engine, date_map)
    logger.info("Data Loaded into Cleaned NYC_Taxi_Data")


# from sqlalchemy import create_engine, text
# from etl.db_config import DB_URL
# from etl.logger import get_logger

# logger = get_logger()

# def load_data(df):
#     logger.info("Starting flat table load")

#     engine = create_engine(DB_URL)

#     # OPTIONAL: make reruns safe
#     with engine.connect() as conn:
#         conn.execute(text("TRUNCATE TABLE fact_nyc_taxi_flat"))
#         conn.commit()

#     df.to_sql(
#         name='fact_nyc_taxi_flat',
#         con=engine,
#         if_exists='append',
#         index=False,
#         chunksize=50_000,
#         method='multi'
#     )

#     logger.info(f"Loaded {len(df)} rows into fact_nyc_taxi_flat")
#     logger.info("Flat table load completed")