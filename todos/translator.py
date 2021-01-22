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
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

        
    # fetch todo from the database
    response= table.get_item(
     Key={
            'id': event['pathParameters']['id']
        }
    )
        
    #extract text from response and translate      
    result = {
        
        'text' : translate.translate_text(Text = response['Item']['text'], 
            SourceLanguageCode ='auto', TargetLanguageCode = event['pathParameters']['language'])
        
    }
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['text'])# + result.get('TranslatedText'),
                          # cls=decimalencoder.DecimalEncoder)
    }

    return response