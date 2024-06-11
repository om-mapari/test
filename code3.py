import os
import boto3
import requests

def lambda_handler(event, context):
    # Retrieve environment variables
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    aws_region = os.environ.get('AWS_REGION')

    # Create a Lambda client using environment variables
    client = boto3.client(
        'lambda',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    # Define the function name
    function_name = 'your_lambda_function_name'

    # Get the Lambda function configuration
    response = client.get_function(FunctionName=function_name)

    # Retrieve the code location
    code_location = response['Code']['Location']

    print(f"Code URL: {code_location}")

    # Download the Lambda function code from the URL
    response = requests.get(code_location)

    # Save the code to a file
    with open('/tmp/lambda_function_code.zip', 'wb') as file:
        file.write(response.content)

    print(f"Lambda function code downloaded successfully.")
    return {
        'statusCode': 200,
        'body': 'Lambda function code downloaded successfully.'
    }
