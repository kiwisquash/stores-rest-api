from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # It's at the root directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # only change flask_sqlalchemy's behavior
app.secret_key = "bobble" # should be longer, and not in file
api = Api(app)

# Here is a method to create all tables before the first request is made! :D
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, "/items/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/stores/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    # We don't want the app to run when another python file imports app.py
    db.init_app(app)
    app.run(port=5000, debug=True)
    # app.run(port=5000, debug=False)
