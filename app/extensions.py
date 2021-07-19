"""Extensions module. Each extension is initialized in the app factory located in __init__.py."""
from flask_mongoengine import MongoEngine
from flask_pymongo import pymongo
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

CONNECTION_STRING = "mongodb+srv://matt-admin:Xf2ZNfUbveQVyWQa@cluster0.pzxrj.mongodb.net/clients?retryWrites=true&w=majority"

mongo_engine = MongoEngine()
mongo_client = pymongo.MongoClient(CONNECTION_STRING)

csrf_protect = CSRFProtect()

login_manager = LoginManager()
