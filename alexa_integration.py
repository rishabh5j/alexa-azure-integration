"""Entry point for Alexa to Azure ARM template integration utility."""

import os
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from flask import Flask
from flask_ask_sdk.skill_adapter import SkillAdapter

from intent_handler import *

logger = logging.getLogger(__name__) # initiate logging handler
logger.setLevel(logging.INFO)

context = ('certificate.pem', 'private-key.pem') # associate SSL certificate with the flask context


# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.
sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(CreateIntentReflectorHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

app = Flask(__name__)
skill_response = SkillAdapter(
    skill=sb.create(),
    skill_id=os.environ["ALEXA_SKILL_ID"],
    app=app, verifiers=[])

skill_response.register(app=app, route="/api") # Route API calls to /api towards skill response

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = "443",debug=True,threaded=True,ssl_context=context)
