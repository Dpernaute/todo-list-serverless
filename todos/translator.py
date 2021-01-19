import os
import json
import time
import logging
from todos import decimalencoder
from todos import get
import boto3

dynamodb = boto3.resource('dynamodb')
translate = boto3.client('translate')

def translator(event, context):
    
    Target_language = "auto"
    data = json.loads(event['body'])
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    
        
    # fetch todo from the database
    response= table.get_item(
     Key={
            'id': event['pathParameters']['id']
        }
    )
        
            
    result = translate.translateText(data['text'], 
            Target_language, data['language'])
    
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps("Translated text: ", #+ result.get('TranslatedText'),
                           cls=decimalencoder.DecimalEncoder)
    }

    return response