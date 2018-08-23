from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#normally use a DB
users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"

      },
      {

        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"

      },
      {

        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"

      }
    ]

class User(Resource):

  #search for user if name is speficied then return user with 200 OK else 404 not found
  def get(self, name):
    for user in users:
      if(name==user["name"]):
        return user, 200
    return "User not found", 404

  #create parser with reqparser, add age and occupation arguments, store parses, if user exists API wil return with 400 bad request
  def post(self, name):
    parser = reqparse.RequestParser()
    parser.add_argument("age")
    parser.add_argument("occupation")
    args = parser.parse_args()

    for user in users:
      if(name == user["name"]):
        return "User with name {} already exists.".format(name), 400

    user = {
      "name": name,
      "age": args["age"],
      "occupation": args["occupation"]
    }
    users.append(user)
    return user, 201

  #if the user already exists update details with parsed arguments and return the user along with a 200 OK else create a user with 201
  def put(self, name):
    parser = reqparse.RequestParses()
    parser.add_argument("age")
    parser.add_argument("occupation")
    args = parser.parse_args()

    for user in users:
      if(name == user["name"]):
        user["age"] = args["age"]
        user["occupation"] = args["occupation"]
        return user, 200

    user = {
        "name": name,
        "age": args["age"],
        "occupation": args["occupation"]
    }
    users.append(user)
    return user, 201

  def delete(self, name):
    global users
    users = [user for user in users if user["name"] != name]
    return "{} is deleted".format(name), 200


api.add_resource(User, "/user/<string:name>")
app.run(debug=True)
