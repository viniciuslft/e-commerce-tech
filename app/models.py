from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'login'


    id_login = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwordhash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.passwordhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordhash, password)