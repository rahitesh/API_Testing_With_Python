import requests
import json
import jsonpath


def test_patch_user_job():

    url="https://reqres.in/api/users/2"

    data = {

        "job" : "Software developer in Test"
    }


    job_json = json.dumps(data)

    response = requests.patch(url, job_json)

    response.raise_for_status()

    statusCode = response.status_code
    
    assert statusCode == 200

    print(response.content)