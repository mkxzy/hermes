from pymongo import MongoClient

class Repository:
    def __init__(self, connection):
        self.connection = connection
        self.database = 'boktour'

    def save(self, collection, data):
        client = MongoClient('mongodb://xiezhiyan:yilvxzy@120.26.246.185:27017/')
        client.get_database(self.database).get_collection(collection).insert(data)