import requests
import argparse
import json

def main(string_data, int_data):
    print("Code started.")
    url = 'http://3.214.88.86:80/run_code'
    headers = {'Content-Type': 'application/json'}
    data = {
        'string_data': string_data,
        'int_data': int_data,
        }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f'Status code: {response.status_code}')
        # Try to parse JSON response
        try:
            response_json = response.json()
            print(response_json)
        except requests.exceptions.JSONDecodeError:
            print('Response is not in JSON format')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('string_data', type=str, help='A string input')
    parser.add_argument('int_data', type=int, help='An integer input')
    
    args = parser.parse_args()
    main(args.string_data, args.int_data)