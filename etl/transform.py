from etl.logger import get_logger
import pandas as pd


logger = get_logger()

def transform_data(df):
    logger.info("Transforming data started")
    # Fixing Data Types
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'],errors ='coerce')
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'],errors ='coerce')
    df['passenger_count'] = pd.to_numeric(df['passenger_count'],errors ='coerce').fillna(0).astype('Int64')

    # Data Quality rules
    df = df[df['total_amount'] >= 0]
    df = df[df['fare_amount'] >= 0]
    df = df[df['tip_amount'] >= 0]
    df = df[df['trip_distance'] > 0]
    df = df[df['tpep_dropoff_datetime'] >= df['tpep_pickup_datetime']]

    # standardize column names
    df = df.rename(columns = {
        'tpep_pickup_datetime': 'pickup_datetime',
        'tpep_dropoff_datetime': 'dropoff_datetime',
        'PULocationID': 'pickup_location_id',
        'DOLocationID': 'dropoff_location_id',
        'payment_type': 'payment_id',
    })

    # Derived Columns
    df['trip_duration_sec'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds()
    df['year'] = df['pickup_datetime'].dt.year
    df['month'] = df['pickup_datetime'].dt.month
    df['date'] = df['pickup_datetime'].dt.date
    df['day'] = df['pickup_datetime'].dt.day_name()
    df['day_type'] = df['day'].apply(lambda x : 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')

    # select required columns
    df = df[
        [
            'pickup_datetime',
            'dropoff_datetime',
            'passenger_count',
            'trip_distance',
            'fare_amount',
            'tip_amount',
            'total_amount',
            'trip_duration_sec',
            'year',
            'month',
            'date',
            'day',
            'day_type',
            'payment_id',
            'pickup_location_id',
            'dropoff_location_id'
        ]
    ]

    logger.info("Transforming data completed")
    return df
