from flask import Flask, request, jsonify
from RunModelsOllama import run_prompt as llm_function

app = Flask(__name__)

# Define a route for the API
@app.route('/run_code', methods=['POST'])
def run_code():
    # Extract the input data from the request
    input_data = request.json
    
    integer_value = input_data.get('int_data')
    string_value = input_data.get('string_data')

    # Call the LLM function with the input data
    result = llm_function(integer_value, string_value)
    
    # Return the result as a JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
