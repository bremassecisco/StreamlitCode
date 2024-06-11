import requests
import json

url = 'http://3.214.88.86:5000/run_code'
headers = {'Content-Type': 'application/json'}
data = {'input_data': 'Please clarify whether or not corn is a fruit or a vegetable.'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
