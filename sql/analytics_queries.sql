select d.full_date,count(*) from fact_nyc_taxi_data f
join dim_date d on
f.date_id = d.date_id
group by d.full_date
order by d.full_date
limit 5;


select d.full_date,round(sum(total_amount)) from fact_nyc_taxi_data f
join dim_date d on
f.date_id = d.date_id
group by d.full_date
order by d.full_date
limit 5;

SELECT 
    pickup_location_id,
    COUNT(*) AS total_trips
FROM fact_nyc_taxi_data
GROUP BY pickup_location_id
ORDER BY total_trips DESC
LIMIT 10;