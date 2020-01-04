# import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True, help="This field cannot be blank.")
        parser.add_argument("password", type=str, required=True, help="This field cannot be blank.")

        data = parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "The username is taken!"}, 409

        user = UserModel(**data)
        user.save_to_db()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data["username"], data["password"]))
        #
        # connection.commit()
        # connection.close()

        return {"message": "User created successfully."}, 201
