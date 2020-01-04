# import sqlite3
from db import db

class UserModel(db.Model):

    # Tells SQLALchemy which table this should be saved to
    __tablename__ = 'users'

    # Tells SQLAlchemy which columns our table should have
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)) # optional limit to the number of characters
    password = db.Column(db.String(80))

    # The columns must match the UserModel's properties in order for data to be saved
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    # You could write this with just "self", but it wouldn't be used anywhere
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

        # Connect to DB
        # connection = sqlite3.connect("data.db")

        # Create a cursor
        # cursor = connection.cursor()

        # Look for the username
        # query = "SELECT * FROM users WHERE username = ?"

        # Run query (must pass a tuple...)
        # result = cursor.execute(query, (username,))

        # Get the first row that matches
        # row = result.fetchone()

        # Create User object if there is a hit
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None

        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE id = ?"
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user

