import json

def lambda_handler(event, context):
    print('12236778s')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
