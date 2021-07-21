import logging
import json
import base64
import azure.functions as func

def main(msg: func.QueueMessage) -> None:
    msg_body = msg.get_body().decode('utf-8')
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg_body)
    data = base64.b64decode(msg_body).decode()
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg_body)
    data_json = json.loads(data)
    return None