# for get data 
import requests
import json

URL = "http://127.0.0.1:8000"
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)

    Request = requests.get(url=URL, data=json_data)

    Response = Request.json()
    print(Response)

get_data()