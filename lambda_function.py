from __future__ import print_function

import json

print('Loading function')


def lambda_handler(event, context):
    print("Hello world" + event)
    return event['key1']
