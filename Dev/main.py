from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
#define the location of our database. database.db is the name of the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
db = SQLAlchemy(app)

#Define the schema/model of the database entries
class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)#primary_key means that this parameter is unique for each entry (HAVE TO CHANGE THIS)
	name = db.Column(db.String(100), nullable=False)#nullable=False: means that this parameter has always to be filled in an entry
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"

#Create the database
db.create_all()

#Validate the request: it has to have the following args when calling a PUT request
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

#Validate the request: it should have at least one of the following args when calling a UPDATE request
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

#Defines how the object will be returned. Mimics the Model/Schema of the database
resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class Video(Resource):
	@marshal_with(resource_fields)#specifies that the "result" value will be displayed/serialized in the way described in resource_fields 
	def get(self, video_id):
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find video with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()

		result = VideoModel.query.filter_by(id=video_id).first()#Makes a GET request with the vid_id we want to POST
		if result:#If there is a result, then the video was already posted
			abort(409, message="Video id taken...")

		#Otherwise, we can go ahead and post the video by reading the request args
		video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
		#Add the video to the database
		db.session.add(video)
		db.session.commit()

		#Return the POST info and the correct operation code
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Video doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result


	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)