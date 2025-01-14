import requests


def test_delete_user():

    url = "https://reqres.in/api/users/2"  #API ENDPOINT

    response = requests.delete(url)   #Delete Request

    statusCode = response.status_code  #get Status code from response

    assert statusCode == 204   # Validate status code