SELECT  zlp."Zone" AS zlp,
        zld."Zone" AS zld,
        MAX(tip_amount)
FROM public.green_taxi_trips AS tt
LEFT JOIN public.taxi_zone_lookup AS zlp ON zlp."LocationID"=tt."PULocationID"
LEFT JOIN public.taxi_zone_lookup AS zld ON zld."LocationID"=tt."DOLocationID"
WHERE DATE(lpep_pickup_datetime) BETWEEN '2019-09-01' AND '2019-09-30' AND zlp."Zone" = 'Astoria'
GROUP BY    zlp."Zone",
            zld."Zone"
ORDER BY MAX(tip_amount) DESC
LIMIT 5;
