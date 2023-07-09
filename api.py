from flask import Flask, jsonify
from flask_restful import Resource, Api, fields
from flask_pymongo import PyMongo
 

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

# mongo db connection
app.config["MONGO_URI"] = "mongodb+srv://mscheruvathur:ycfmpibwmlfn@api.vr32mce.mongodb.net/api?retryWrites=true&w=majority"
db = PyMongo(app).db


user = {
    "name" : fields.String,
    "email" : fields.String,
    "mobile" : fields.String,
    "designation" : fields.String
}



def add_user(name, email, mobile, designation, active):
    user = db.user.insert_one({
        "name" : name,
        "email" : email,
        "mobile" : mobile,
        "designation" : designation
    })

    return name


# user base class
class UserController (Resource):
    def get(self):
        user = db.user.find({"name": "sam"})
        data = []

        for use in user:
            data.append(use)

        del data[0]['_id']
        return data[0]

    def post (self):
        user = add_user(name="sam", email="mscheruvathur@gmail.com", mobile="+91799411515", designation="Team lead")        
        
        return f'Hi {user} your registration completed successfully'



# api routes
api.add_resource(UserController, '/')




if __name__ == "__main__":
    app.run(debug=True, port=3001)