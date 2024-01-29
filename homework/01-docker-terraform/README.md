---

[Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/01-docker-terraform/homework.md)

**Question 1. Knowing docker tags**

Run the command to get information on Docker

docker --help

Now run the command to get help on the "docker build" command:

docker build --help

Do the same for "docker run".

Which tag has the following text? - Automatically remove the container when it exits

--delete</br>
--rc</br>
--rmc</br>
**<u>--rm</u>**


**Question 2. Understanding docker first run**

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash. Now check the python modules that are installed ( use pip list ).

What is version of the package wheel ?

**<u>0.42.0</u>**</br>
1.0.0</br>
23.0.1</br>
58.1.0</br>



**Prepare Postgres**
---

Run Postgres and load data as shown in the videos We'll use the green taxi trips from September 2019:

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz

You will also need the dataset with zones:

wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)

**Question 3. Count records**

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18.

Remember that lpep_pickup_datetime and lpep_dropoff_datetime columns are in the format timestamp (date and hour+min+sec) and not in date.

15767</br>
**<u>15612</u>**</br>
15859</br>
89009</br>

Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

Tip: For every trip on a single day, we only care about the trip with the longest distance.

2019-09-18</br>
2019-09-16</br>
2019-09-26</br>
2019-09-21


**<u>"2019-09-21"	135.53</u>**</br>


**Question 5. Three biggest pick up Boroughs**

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

**<u>"Brooklyn" "Manhattan" "Queens"</u>**</br>
"Bronx" "Brooklyn" "Manhattan"</br>
"Bronx" "Manhattan" "Queens"</br>
"Brooklyn" "Queens" "Staten Island"</br>


**Question 6. Largest tip**

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

Note: it's not a typo, it's tip , not trip

Central Park</br>
Jamaica</br>
**<u>JFK Airport</u>**</br>
Long Island City/Queens Plaza</br>




**<u>Apply complete! Resources: 1 added, 0 changed, 0 destroyed.**</br>