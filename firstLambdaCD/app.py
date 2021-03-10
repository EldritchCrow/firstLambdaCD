
def lambda_function(event, context):
    message = 'Hello {} {}!'.format(event['obj_name'], 
                                    event['body'])  
    return { 
        'message' : message
    }  
    
