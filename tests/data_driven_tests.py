import requests
import pytest
import csv

test_data_zip_codes = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("ire", "12345", "Dublin")
]

'''
# @pytest.mark.parametrize marker - two args - maps elements in tuple, test data object
# Will run test three times - once for each tuple in test data object
@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name
'''

# This method opens the .csv file in reading mode, skips the header row, adds all other lines to the list of test data values test_data one by one and returns the test data object.
def read_test_data_from_csv():
    test_data = []
    with open("test_data/test_data_zip_codes.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)
        for row in data:
            test_data.append(row)
    return test_data

@pytest.mark.parametrize("country_code, zip_code, expected_place_name", read_test_data_from_csv())
def test_using_csv_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name
