import json

def lambda_handler(event, context):
    print('Hello!!!!!!!!!!!!!!!!!!!!!!!!122')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
