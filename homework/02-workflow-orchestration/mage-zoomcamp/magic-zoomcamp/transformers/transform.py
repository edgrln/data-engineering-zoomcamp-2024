if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Preprocessing: rows with zero passengers:", data['passenger_count'].isin([0]).sum())
    data = data[data['passenger_count'] > 0]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date 
    data = data[data['trip_distance'] != 0]

    columns_for_renaming = {'VendorID': 'vendor_id' ,                
                    'RatecodeID':'ratecode_id',
                    'PULocationID': 'pu_location_id',
                    'DOLocationID': 'do_location_id',
                    }
    data.rename(columns=columns_for_renaming)
    return  data



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' not in output.columns, 'There are rides with zero passengers'
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero passengers'
