import requests
import json
import jsonpath
import datetime
import pytest

def test_create_user():

    url = "https://reqres.in/api/users"   #API endpoint

    json_file = open("data/user_details.json", "r")  # Open the file where have the post request data

    jsn_input = json_file.read()  # read file and save it in variable

    request_json = json.loads(jsn_input)   # Parse it into Json

    response = requests.post(url, request_json)  # post request

    statusCode = response.status_code  #get status code

    content_text = response.text #get respnse content in text

    content_json = json.loads(content_text) # parse it into json 

    created_date = jsonpath.jsonpath(content_json, "createdAt")  # get created date from response

    filterd_date = created_date[0].split("T")[0]    # get the date removeing time

    now = datetime.datetime.today()    # get current system date

    formatted_date = now.strftime("%Y-%m-%d")   # formate it like response date

    assert str(filterd_date) == str(formatted_date)  # both dates should match
  
    assert statusCode == 201   # validate status code for Post request


def test_login_unsuccessful():

    url = "https://reqres.in/api/login"

    login_data = {
        
        "email": "eve.holt@reqres.in"
    }

    respons = requests.post(url, data=json.dumps(login_data))

    statusCode = respons.status_code

    assert statusCode == 400

    resp_text = respons.text

    resp_json = json.loads(resp_text)

    err = jsonpath.jsonpath(resp_json, "error")

    assert "Missing" in  err[0]

    
