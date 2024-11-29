
from database import database

database.articles.update_many({}, [{'$set': {'language': 'en'}}])