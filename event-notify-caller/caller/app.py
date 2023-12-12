import boto3
import os
DESTINATION_PHONE_NUMBER=os.environ['DESTINATION_PHONE_NUMBER']
CONTACT_FLOW_ID=os.environ['CONTACT_FLOW_ID']
INSTANCE_ID=os.environ['AMAZON_CONNECT_INSTANCE_ID']
SOURCE_PHONE_NUMBER=os.environ['SOURCE_PHONE_NUMBER']


def lambda_handler(event, context):

    if 'queryStringParameters' in event:
        queries = event['queryStringParameters']
        body = queries['withdraw']
    else:
        return {
            "statusCode": 503,
            "body": "Failed",
            "headers": {
                "content-type": "application/json"
            },
            "isBase64Encoded": False
        }

    # Amazon Connectでフローを開始する
    client = boto3.client('connect')
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber=DESTINATION_PHONE_NUMBER,
        ContactFlowId=CONTACT_FLOW_ID,
        InstanceId=INSTANCE_ID,
        SourcePhoneNumber=SOURCE_PHONE_NUMBER,
        Attributes={
            'withdraw': body # Amazon Connectでフローを開始する際に受け渡す。引き落としイベント名。
        }
    )

    return {
        "statusCode": 200,
        "body": "Success",
        "headers": {
            "content-type": "application/json"
        },
        "isBase64Encoded": False
    }