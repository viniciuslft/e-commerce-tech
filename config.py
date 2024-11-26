import os

class Config: 
    SECRET_KEY = '4b7f6d2e1c9a8b7f6d2e1c9a8b7'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres:conta1dalive@localhost:5432/EcommerceADS')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
