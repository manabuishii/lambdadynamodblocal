import sys
import os
import uuid
import boto3
endpoint_url = os.getenv('DYNAMO_ENDPOINT', None)
dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
user_table = dynamodb.Table('user')
user = {
"UserID": str(uuid.uuid4()),
"UserName": "Tokyo Skytree"
}
user_table.put_item(Item=user)

def handler(event, context): 
    return 'Hello v0.5.0 from AWS Lambda using Python' + sys.version + '!'