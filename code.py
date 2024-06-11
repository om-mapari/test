import boto3

def get_lambda_function_code(function_name):
    # Create a Lambda client
    client = boto3.client('lambda')

    # Get the Lambda function configuration
    response = client.get_function(FunctionName=function_name)

    # Retrieve the code location
    code_location = response['Code']['Location']

    print(f"Code URL: {code_location}")

    return code_location

# Replace 'your_lambda_function_name' with your actual Lambda function name
function_name = 'your_lambda_function_name'
code_url = get_lambda_function_code(function_name)

# Download the Lambda function code from the URL
import requests

response = requests.get(code_url)

# Save the code to a file
with open('lambda_function_code.zip', 'wb') as file:
    file.write(response.content)

print(f"Lambda function code downloaded successfully.")
