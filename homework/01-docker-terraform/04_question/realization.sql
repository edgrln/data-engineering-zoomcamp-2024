SELECT DATE(lpep_pickup_datetime), 
        max(trip_distance)
FROM public.green_taxi_trips
WHERE DATE(lpep_pickup_datetime) = DATE(lpep_dropoff_datetime)
GROUP BY DATE (lpep_pickup_datetime)
ORDER BY max(trip_distance) DESC
LIMIT 5;
