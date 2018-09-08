from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

# class User(Resource):
#     def post(self):
#         response = {
#             "version": "1.0",
#             "response": {
#                 "outputSpeech": {
#                     "type": "PlainText",
#                     "text": "Hello all, this is a sample text for testing purpose",
# 
#                 },
#                 "card": {
#                     "type": "Simple",
#                     "title": "Testing Purpose",
#                     "content": "Nothing much content",
#                 },
#                 "reprompt": {
#                     "outputSpeech": {
#                         "type": "PlainText",
#                         "text": "Can i help you with anything else.",
# 
#                     }
#                 },
#             }
#         }
#         return response
# 
# 
# api.add_resource(User, '/user')
# app.run()
	