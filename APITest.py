import requests
import json

def main():
    print("Code started.")
    url = 'http://10.11.3.236:5000/run_code'
    headers = {'Content-Type': 'application/json'}
    data = {'input_data': 'Please clarify whether or not corn is a fruit or a vegetable.'}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    main()
