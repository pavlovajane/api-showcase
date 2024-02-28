import boto3

sqs = boto3.client('sqs')
queue_url = "https://sqs.us-east-2.amazonaws.com/339572481413/SQS-api-showcase"

def send_message(data):
# Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageBody=data
    )

    return response['MessageId']