from flask import Flask, request
from flask import jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
    return 'Hellow orlds!!!'


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
			"shouldEndSession": False
        }
    }
    return jsonify(response), 201

@app.route('/user/full', methods=['POST'])
def post_testing_full():
  result = {
  "version": "1.0",
  "sessionAttributes": {
    "supportedHoriscopePeriods": {
      "daily": True,
      "weekly": False,
      "monthly": False
    }
  },
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "Today will provide you a new learning opportunity.  Stick with it and the possibilities will be endless. Can I help you with anything else?"
    },
    "card": {
      "type": "Simple",
      "title": "Horoscope",
      "content": "Today will provide you a new learning opportunity.  Stick with it and the possibilities will be endless."
    },
    "reprompt": {
      "outputSpeech": {
        "type": "PlainText",
        "text": "Can I help you with anything else?"
      }
    },
    "shouldEndSession": False
   }
  }
  return jsonify(result)
  
@app.route('/user/msd', methods=['POST'])
def msd_post():
  intent = request.get_json(silent=True)
  if intent["request"]["intent"]["name"] == 'GetNewFactIntent':
    result = {
  "version": "1.0",
  "sessionAttributes": {
    "supportedHoriscopePeriods": {
      "daily": True,
      "weekly": False,
      "monthly": False
    }
  },
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "Today will provide you a new learning opportunity.  Stick with it and the possibilities will be endless. Can I help you with anything else?"
    },
    "card": {
      "type": "Simple",
      "title": "Horoscope",
      "content": "Today will provide you a new learning opportunity.  Stick with it and the possibilities will be endless."
    },
    "reprompt": {
      "outputSpeech": {
        "type": "PlainText",
        "text": "Can I help you with anything else?"
      }
    },
    "shouldEndSession": False
   }
  }
    return jsonify(result)
  
  elif intent["request"]["intent"]["name"] == 'CricketIntent':
    result = {
  "version": "1.0",
  "sessionAttributes": {
    "supportedHoriscopePeriods": {
      "daily": True,
      "weekly": False,
      "monthly": False
    }
  },
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "MSD is a great cricketer"
    },
    "card": {
      "type": "Simple",
      "title": "MSD",
      "content": "MSD is a great cricketer"
    },
    "reprompt": {
      "outputSpeech": {
        "type": "PlainText",
        "text": "Can I help you with anything else?"
      }
    },
    "shouldEndSession": False
   }
  }
    return jsonify(result)
  else:
    result = {
  "version": "1.0",
  "sessionAttributes": {
    "supportedHoriscopePeriods": {
      "daily": True,
      "weekly": False,
      "monthly": False
    }
  },
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "May be I need to update my dictionary to answer you. Your're brilliant than me."
    },
    "card": {
      "type": "Simple",
      "title": "Oh!!",
      "content": "May be I need to update my dictionary to answer you. Your're brilliant than me."
    },
    "reprompt": {
      "outputSpeech": {
        "type": "PlainText",
        "text": "Can I help you with anything else?"
      }
    },
    "shouldEndSession": False
   }
  }
    return jsonify(result)  
    
	
	
# api.add_resource(User, '/user')
if __name__=='__main__':
    app.run(debug=True)
