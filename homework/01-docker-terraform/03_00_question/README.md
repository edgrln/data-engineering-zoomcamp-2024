
# Commands for launch and stop PostgreSQL and PgAdmin
```bash
docker compose build # build images
docker compose up -d # create and start containers
docker compose down --remove-orphans # Stop and remove containers, networks 
```


# Commands for creating Python virtual environment for debugging
```shell script
python3 -m venv venv
```

```shell script
source venv/bin/activate
```

```bash
pip3 install -r requirements.txt
```

# Links with datasets

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz

You will also need the dataset with zones:

wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv


# Commands for data ingestion

```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"
```


```bash
python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=green_taxi_trips \
  --url=${URL}
  ```


```bash
URL="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"
```

```bash
python ingest_data_zone_lookup.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=taxi_zone_lookup \
  --url=${URL}
  ```



