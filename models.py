from app import db

class UserModelgit (db.Document):
    cpf = db.StringField(required=True,unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(reuired=True)
    birth_date = db.DateTimeField(required=True)