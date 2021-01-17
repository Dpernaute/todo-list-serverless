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
    
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't translate the todo item.")
        return
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    
    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    logger.info(result)
    
    if 'Item' in result:
        return result
        
    except Exception as e:
    logger.error(result)
    raise Exception("[ErrorMessage]: " + str(e))    
    
    TranslatedText = translate.translate_text( data['text'], Target_language, event['pathParameters']['language'])
        
    logging.info("Translation output: " + str(TranslatedText))
    except Exception as e:
    logger.error(result)
    raise Exception("[ErrorMessage]: " + str(e))
        
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response