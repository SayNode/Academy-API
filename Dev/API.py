from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from thor_requests import init, wallet_import_1, wallet_import_2, wallet_balance, transfer_DHN, main

app = Flask(__name__)
api = Api(app)

#Validate the request: it has to have the following args when calling a PUT request
form_put_args = reqparse.RequestParser()
form_put_args.add_argument("User_ID", type=str, help="User_ID of the form is required", required=True)
form_put_args.add_argument("Quiz_ID", type=str, help="Quiz_ID of the form", required=True)

#Validate the request: it should have at least one of the following args when calling a UPDATE request
form_update_args = reqparse.RequestParser()
form_update_args.add_argument("Reward", type=int, help="Reward payed")
form_update_args.add_argument("Completed", type=bool, help="Quiz Completed")

class Form(Resource):
	
	def get(self, wallet_id, reward):
		return {"wallet_id": wallet_id, "reward": reward}


api.add_resource(Form, "/form/<string:wallet_id>/<int:reward>")

if __name__ == "__main__":
	app.run(debug=True)