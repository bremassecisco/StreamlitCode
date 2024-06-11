import requests
import json

def main():
    print("Code started.")
    url = 'http://127.0.0.1:5000/run_code'
    headers = {'Content-Type': 'application/json'}
    data = {
        'string_data': 'Please clarify whether or not corn is a fruit or a vegetable.',
        'int_data': 2,
        }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f'Status code: {response.status_code}')
        
        # Print the raw response content for debugging
        print('Raw response content:', response.text)
        
        # Try to parse JSON response
        try:
            response_json = response.json()
            print(response_json)
        except requests.exceptions.JSONDecodeError:
            print('Response is not in JSON format')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()