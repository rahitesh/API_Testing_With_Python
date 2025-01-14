import requests
import json
import jsonpath

def test_fetch_user_details():

    url = "https://reqres.in/api/users?page=2"

    response = requests.get(url)

    statusCode = response.status_code

    json_data = json.loads(response.text)

    first_name = jsonpath.jsonpath(json_data, "data[0].first_name")

    email  = jsonpath.jsonpath(json_data, "data[0].email")

    assert first_name[0] == "Michael"

    assert email[0] == "michael.lawson@reqres.in"

    assert statusCode == 200
    