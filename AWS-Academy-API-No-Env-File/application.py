from email.mime import application
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from decouple import config
import vechain_txs 
import os

application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return 'Unidentified API'
   
class Form(Resource):
	
	def get(self, wallet_id, reward, api_key):
		PRIVATE_KEY = os.environ['PRIVATE_KEY']
		if PRIVATE_KEY != api_key:
			abort(401, message="Wrong API key")
		vechain_txs.main(wallet_id,reward)
		return reward+" DHN tokens were awarded to the following wallet address: "+ wallet_id

class Balances(Resource):
	def get(self, wallet_id_one, wallet_id_two):
		(balance_one, balance_two)=vechain_txs.balances(wallet_id_one, wallet_id_two)
		return "Wallet1("+wallet_id_one+"):"+ str(balance_one) + \
			   "                         Wallet2("+wallet_id_two+"):"+str(balance_two)
		

api.add_resource(Form, "/form/<string:wallet_id>/<string:reward>/<string:api_key>")
api.add_resource(Balances, "/balances/<string:wallet_id_one>/<string:wallet_id_two>")

if __name__ == "__main__":

	application.run()