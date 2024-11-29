import mongoengine as me
import pymongo


me.connect(host="mongodb://mongo:27017/coderabbittest")
db_client: pymongo.MongoClient = me.connection.get_connection()
database = db_client.get_default_database()