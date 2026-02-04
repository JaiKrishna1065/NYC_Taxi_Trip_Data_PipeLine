CREATE TABLE fact_trips (
    pickup_datetime DATETIME,
    dropoff_datetime DATETIME,

    passenger_count INT,
    trip_distance FLOAT,
    fare_amount FLOAT,
    tip_amount FLOAT,
    total_amount FLOAT,
    trip_duration_sec INT,

    date_id INT,
    pickup_location_id INT,
    dropoff_location_id INT,
    payment_type INT,

    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (pickup_location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (dropoff_location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (payment_type) REFERENCES dim_payment(payment_type)
);


-- without star schema
-- CREATE TABLE fact_nyc_taxi_flat (
--     pickup_datetime DATETIME,
--     dropoff_datetime DATETIME,

--     passenger_count INT,
--     trip_distance FLOAT,

--     fare_amount FLOAT,
--     tip_amount FLOAT,
--     total_amount FLOAT,

--     trip_duration_sec FLOAT,

--     year INT,
--     month INT,
--     day VARCHAR(10),
--     day_type VARCHAR(10),

--     payment_id INT,
--     pickup_location_id INT,
--     dropoff_location_id INT
-- );

-- CREATE INDEX idx_pickup_date 
-- ON fact_nyc_taxi_flat(pickup_datetime);

-- CREATE INDEX idx_pickup_location
-- ON fact_nyc_taxi_flat(pickup_location_id);

-- CREATE INDEX idx_payment
-- ON fact_nyc_taxi_flat(payment_id);
