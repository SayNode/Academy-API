from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import re
import vechain_txs 

app = Flask(__name__)
api = Api(app)

class Form(Resource):
	
	def get(self, wallet_id, reward):

		regex_check = re.match(r'^0x[a-fA-F0-9]{40}$',wallet_id)# see if wallet address is correct format

		if wallet_id != None:
			vechain_txs.main(wallet_id,reward)
			return reward+" DHN tokens were awarded to the following wallet address: "+ wallet_id
		else:
			return "Wallet address is not valid"


api.add_resource(Form, "/form/<string:wallet_id>/<string:reward>")

if __name__ == "__main__":
	app.run(debug=True)