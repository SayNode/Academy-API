from email.mime import application
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import vechain_txs 

application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return 'Hello'
    
class Form(Resource):
	
	def get(self, wallet_id, reward):

		vechain_txs.main(wallet_id,reward)
		return reward+" DHN tokens were awarded to the following wallet address: "+ wallet_id


api.add_resource(Form, "/form/<string:wallet_id>/<string:reward>")

if __name__ == "__main__":
	application.run()