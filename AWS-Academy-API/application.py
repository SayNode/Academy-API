from email.mime import application
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from decouple import config
import vechain_txs 

application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return 'Unidentified API'
   
class Form(Resource):
	
	def get(self, wallet_id, reward, api_key):
		PRIVATE_KEY = config('PRIVATE_KEY')
		if PRIVATE_KEY != api_key:
			abort(401, message="Wrong API key")
		vechain_txs.main(wallet_id,reward)
		return reward+" DHN tokens were awarded to the following wallet address: "+ wallet_id


api.add_resource(Form, "/form/<string:wallet_id>/<string:reward>/<string:api_key>")

if __name__ == "__main__":

	application.run()