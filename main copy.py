# Step 1 is to install the requirement file: pip3 install pip3 install -r requirements.txt
# Then import flask and flask restfull
from flask import Flask
from flask_restful import Api, Resource


# Initialize Flask app
app = Flask(__name__)
# Wrap app in Api
api = Api(app)


# Next let's create our first resource, this class inherit from Resource. We will list all actions functions.
class HelloWorld(Resource):
    def get(self):
        return {"data": "HelloWorld"}
    
    def post(self):
        return {"data":"posted"}
    
# Add resource to API. The first passed argument is the resource to add followed by the endpoint to reach the resource
api.add_resource(HelloWorld, "/helloworld")

# Run the application and set debug mode to true to visualize dev logs. 
# Do not use "debug-True" if in production environment
if __name__ == "__main__":
    app.run(debug=True)
    
# At this point you can run the app by running the main file: pyhton3 main.py

