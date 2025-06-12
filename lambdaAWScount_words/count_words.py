import boto3
import os

sns_client = boto3.client('sns')
s3_client = boto3.client('s3')

SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3_client.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    word_count = len(content.split())

    message = f"The word count in the {key} file is {word_count}."
    subject = "Word Count Result"

    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )

    return {
        'statusCode': 200,
        'body': message
    }
