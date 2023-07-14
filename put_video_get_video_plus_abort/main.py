from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Viewsv of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

videos = {
}


def abort_video_id_dont_exist(video_id):
    if video_id not in videos:
        abort(404 , message="The video id does not exist")
        

# Classes containing requests
class Video(Resource):
    def get(self, video_id):
        abort_video_id_dont_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 
        
        
# Pass arguments through the requested url. Could be <string> || <int> , ect
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
    

