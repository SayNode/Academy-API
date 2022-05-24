from email.mime import application
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from decouple import config
import vechain_txs 
import os


application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return 'Unidentified API'

#Execute reward transfer of a certain DHN amount to a wallet address  
class Form(Resource):
	
	def get(self, wallet_id, reward, api_key):
		PRIVATE_KEY = os.environ['PRIVATE_KEY']
		if PRIVATE_KEY != api_key:
			abort(403, message="Wrong API key")
		vechain_txs.main(wallet_id,reward)
		return jsonify(
				response_one = reward+" DHN tokens were awarded to the following wallet address: "+ wallet_id,
				status = "200"
			   )

#Get balances of two wallets
class Balances(Resource):
	def get(self, wallet_id_one, wallet_id_two):
		(balance_one, balance_two)=vechain_txs.balances(wallet_id_one, wallet_id_two)
		return jsonify(
				response_one = "Wallet1 ("+wallet_id_one+") DHN balance: "+ str(balance_one/(10**18)),
		 		response_two = "Wallet2 ("+wallet_id_two+") DHN balance: "+str(balance_two/(10**18)),
				status = "200"
			   )
		
api.add_resource(Form, "/form/<string:wallet_id>/<string:reward>/<string:api_key>")
api.add_resource(Balances, "/balances/<string:wallet_id_one>/<string:wallet_id_two>")

if __name__ == "__main__":

	application.run()