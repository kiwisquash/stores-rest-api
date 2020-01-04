from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    # Find the user with the matching user
    user = UserModel.find_by_username(username)

    # Use safe string comparison to check that the passwords match
    # ascii, unicode, etc...
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

