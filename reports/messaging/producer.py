import boto3
import json

sqs = boto3.client('sqs', region_name="us-east-2")
queue_url = "https://sqs.us-east-2.amazonaws.com/339572481413/SQS-api-showcase"

def send_message(data):

    message_body = {
            'report_id': str(data.id)
        }

    response = sqs.send_message(
            MessageBody=json.dumps(message_body),
            MessageId='messageGroupId'
        )


    return response['MessageId']