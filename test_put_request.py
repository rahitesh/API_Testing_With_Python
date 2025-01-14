import requests
import json, jsonpath

def test_update_user_details():

    url = "https://reqres.in/api/users/2"

    file = open("data/user_details.json", "r")

    json_file = file.read()

    json_content = json.loads(json_file)

    response = requests.put(url, json_content)

    statusCode = response.status_code

    assert statusCode == 200

    response_text = response.text

    response_json = json.loads(response_text)

    user_job = jsonpath.jsonpath(response_json, "job")

    assert str(user_job[0]) == "Automation Test Engineer"

