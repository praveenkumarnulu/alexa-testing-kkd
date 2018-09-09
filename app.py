from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
    return 'Hellow orldddddd'+'Nothing mucjhhhhhh'


#
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

@app.route('/user', methods=['POST'])
def post_testing():
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Hello praveen i am here checking ait alllll",

            },
            "card": {
                "type": "Simple",
                "title": "Testing Purpose",
                "content": "Nothing much content",
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Can i help you with anything else.",

                }
            },
        }
    }
    return jsonify(response), 201


# api.add_resource(User, '/user')
app.run()
