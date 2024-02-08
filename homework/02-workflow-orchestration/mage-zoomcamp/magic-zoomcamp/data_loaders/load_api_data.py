import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@data_loader
def load_data_from_api(*args, **kwargs):
    year = 2020
    list_month = [10, 11, 12]

    columns = [     'VendorID',
                    'lpep_pickup_datetime', 
                    'lpep_dropoff_datetime',
                    'store_and_fwd_flag',
                    'RatecodeID',
                    'PULocationID',
                    'DOLocationID',
                    'passenger_count',
                    'trip_distance',
                    'fare_amount',
                    'extra',
                    'mta_tax',
                    'tip_amount',
                    'tolls_amount',
                    'ehail_fee',
                    'improvement_surcharge',
                    'total_amount',
                    'payment_type',
                    'trip_type',
                    'congestion_surcharge']

    data = pd.DataFrame(columns=columns)

    for month in list_month:
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_{year}-{month}.csv.gz'

        taxi_dtypes = { 
                        'VendorID': pd.Int64Dtype(),
                        # 'lpep_pickup_datetime': pd.Int64Dtype(),
                        # 'lpep_dropoff_datetime': float,
                        'store_and_fwd_flag': str,
                        'RatecodeID': pd.Int64Dtype(),
                        'PULocationID': pd.Int64Dtype(),
                        'DOLocationID': pd.Int64Dtype(),
                        'passenger_count': pd.Int64Dtype(),
                        'trip_distance': float,
                        'fare_amount': float,
                        'extra': float,
                        'mta_tax': float,
                        'tip_amount': float,
                        'tolls_amount': float,
                        'ehail_fee': float,
                        'improvement_surcharge': float,
                        'total_amount': float,
                        'payment_type': pd.Int64Dtype(),
                        'trip_type': pd.Int64Dtype(),
                        'congestion_surcharge': float
                    }
        

         # response = requests.get(url)
        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

        # return pd.read_csv(io.StringIO(response.text), sep=',', compression = 'gzip', dtype = taxi_dtypes)
        df_tmp = pd.read_csv(url, sep=",", compression = "gzip" , dtype = taxi_dtypes, parse_dates=parse_dates)
        data = pd.concat([data, df_tmp])
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
