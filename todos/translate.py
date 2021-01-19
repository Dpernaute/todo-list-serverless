import os
import json
import time
import logging
from todos import decimalencoder
from todos import get
import boto3

dynamodb = boto3.resource('dynamodb')


def translate(event, context):
    
    Target_language = "auto"
    data = json.loads(event['body'])
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    
        
    # fetch todo from the database
    result = table.get_item(
     Key={
            'id': event['pathParameters']['id']
        }
    )
        
        
     
    
            
    logging.info("Translation output: " + translate(data['text'], event['pathParameters']['language']) ['TranslatedText'])
    
    
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps("Translation output: ",
                           cls=decimalencoder.DecimalEncoder)
    }

    return response