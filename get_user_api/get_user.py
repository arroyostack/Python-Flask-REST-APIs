# Step 1 is to install the requirement file: pip3 install pip3 install -r requirements.txt
# Then import flask and flask restful
from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

names = {
    "tim": {"age": 46, "gender":"male"},
    "bill": {"age": 26, "gender":"female"},  
}

# Classes containing requests
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    
    def post(self):
        return {"data":"posted"}
    
# Pass arguments through the requested url. Could be <string> || <int> , ect
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
    

