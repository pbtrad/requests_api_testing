import requests

# HTTP response status code
def test_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200

# Check if the value of the response content type header correctly identifies that the response body is in JSON format
def test_get_locations_for_us_90210_check_content_type_equals_json():
     response = requests.get("http://api.zippopotam.us/us/90210")
     assert response.headers["Content-Type"] == "application/json"

# Check the value of response body element
def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"

# Extract and assert on the value of the place name for the first place in the list of places
def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Beverly Hills"

