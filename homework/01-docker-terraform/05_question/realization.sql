SELECT "Borough", 
        SUM(total_amount)
FROM green_taxi_trips AS tt
LEFT JOIN public.taxi_zone_lookup AS zl ON zl."LocationID" = tt."PULocationID"
WHERE DATE(lpep_pickup_datetime)= '2019-09-18'
GROUP BY "Borough"
ORDER BY SUM(total_amount) DESC
LIMIT 5;
