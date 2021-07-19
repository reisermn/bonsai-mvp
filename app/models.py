import pymongo
from app.extensions import mongo_engine, mongo_client

# To make the implementation of the User class easier
from flask_login import UserMixin

# PyMongo Database
mongo_db = mongo_client.get_database('clients')
mongo_col_company = pymongo.collection.Collection(mongo_db, 'company')
mongo_col_user = pymongo.collection.Collection(mongo_db, 'user')

# MONGODB UTILITIES
# mongo_col_company.create_index("_id")
# mongo_col_company.index_information()
# # WARNING: We don't want mongodb to automatically think that certain indexes should be unique
# mongo_col_company.drop_indexes()


# MongoEngine Classes
class User(UserMixin, mongo_engine.Document):
    name = mongo_engine.StringField(required=True)
    company_name = mongo_engine.StringField(required=True)
    email = mongo_engine.StringField(required=True)
    password = mongo_engine.StringField(required=True)


class Company(mongo_engine.Document):
    name = mongo_engine.StringField(required=True)
    company_name = mongo_engine.StringField(required=True)
    email = mongo_engine.StringField(required=True)
    password = mongo_engine.StringField(required=True)
