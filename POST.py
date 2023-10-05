import os
import json

def post(data, website):
    json_output = json.dumps(data).replace("\"", "\\\"").replace("\'", "\\\'")
    os.system(f"curl -X POST -H \"Content-Type: application/json\" --data \"{json_output}\" {website} > output.txt")

    with open("output.txt") as file:
        s = file.read()
    
    os.remove("output.txt")
    return s

data_register = {
    "method": "create_user",
    "data": {
        "username": "admin",
        "password": "password13"
    }
}

data_login = {
    "method": "get_session_id",
    "data": {
        "username": "admin1",
        "password": "password12"
    }
}

data = data_register

result = post(data, "http://127.0.0.1:5000/endpoint")

print(json.loads(result))