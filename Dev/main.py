from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
#define the location of our database. database.db is the User_ID of the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
db = SQLAlchemy(app)

#Define the schema/model of the database entries
class FormModel(db.Model):
	UI = db.Column(db.String(100), primary_key=True)#primary_key means that this parameter is unique for each entry (HAVE TO CHANGE THIS)
	User_ID = db.Column(db.String(100), nullable=False)#nullable=False: means that this parameter has always to be filled in an entry
	Quiz_ID = db.Column(db.String(100), nullable=False)
	Reward = db.Column(db.Integer, nullable=False)
	Completed = db.Column(db.Boolean, nullable=False)

	def __repr__(self):
		return f"Form(User_ID = {self.User_ID}, Quiz_ID = {self.Quiz_ID}, Reward = {self.Reward})"

#Create the database
db.create_all()

#Validate the request: it has to have the following args when calling a PUT request
form_put_args = reqparse.RequestParser()
form_put_args.add_argument("User_ID", type=str, help="User_ID of the form is required", required=True)
form_put_args.add_argument("Quiz_ID", type=int, help="Quiz_ID of the form", required=True)

#Validate the request: it should have at least one of the following args when calling a UPDATE request
form_update_args = reqparse.RequestParser()
form_update_args.add_argument("Reward", type=int, help="Reward payed")
form_update_args.add_argument("Completed", type=bool, help="Quiz Completed")

#Defines how the object will be returned/serialized (JSON in this case). Mimics the Model/Schema of the database
resource_fields = {
	'UI': fields.String,
	'User_ID': fields.String,
	'Quiz_ID': fields.String,
	'Reward': fields.Integer,
	'Completed': fields.Boolean
}

class Form(Resource):
	@marshal_with(resource_fields)#specifies that the "result" value will be displayed/serialized in the way described in resource_fields 
	def get(self, form_id):
		result = FormModel.query.filter_by(id=form_id).first()
		if not result:
			abort(404, message="Could not find form with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, form_id):
		args = form_put_args.parse_args()

		result = FormModel.query.filter_by(id=form_id).first()#Makes a GET request with the vid_id we want to POST
															    #we have to see if we want just the first() or .all()
		if result:#If there is a result, then the form was already posted
			abort(409, message="Form already exists")

		#Otherwise, we can go ahead and post the form by reading the request args
		form = FormModel(id=form_id, User_ID=args['User_ID'], Quiz_ID=args['Quiz_ID'], Reward=args['Reward'])
		#Add the form to the database
		db.session.add(form)#adds object to the DB session (temporary)
		db.session.commit()#commits the changes permanetly to the DB

		#Return the POST info and the correct operation code
		return form, 201

	@marshal_with(resource_fields)
	def patch(self, form_id):
		args = form_update_args.parse_args()
		result = FormModel.query.filter_by(id=form_id).first()
		if not result:
			abort(404, message="form doesn't exist, cannot update")

		if args['Reward']:
			result.Reward = args['Reward']
		if args['Completed']:
			result.Completed = args['Completed']

		db.session.commit()

		return result

	@marshal_with(resource_fields)
	def delete(self, form_id):
		args = form_update_args.parse_args()
		result = FormModel.query.filter_by(id=form_id).first()
		if not result:
			abort(404, message="form doesn't exist, cannot update")
		del forms[form_id]
		return '', 204


api.add_resource(Form, "/form/<int:form_id>")

if __name__ == "__main__":
	app.run(debug=True)