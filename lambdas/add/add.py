import json

def lambda_handler(event, context):
   print(event)
   first = event['first']
   second = event['second']
   
   result = int(first) + int(second)
   print(f"RESULT: {result}")
   
   response = {
       "result": int(result)
   }
   
   return response
