import json

def lambda_handler(event, context):
    print('Aur bhai')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
