from pymongo import MongoClient
from database.parse_json import ParseJson


class Database:
    def __init__(self, database="test", collection="test"):
        self.host = "localhost"
        self.port = 27017
        self.mongo_client = MongoClient(self.host, self.port, serverSelectionTimeoutMS=1000)
        self._db = self.mongo_client[database]
        self._collection = self._db[collection]

    def insert(self, data):
        try:
            self._collection.insert_one(data)
            print("Data inserted")
            failed = ParseJson('dumps/failed_dumps.json').read()
            if len(failed) > 0:
                try:
                    self._collection.insert_many(failed)
                    ParseJson("dumps/failed_dumps.json").write([])
                    print("Failed dumps inserted")
                except:
                    print("Failed to insert failed dumps")
        except:
            failed = ParseJson('dumps/failed_dumps.json').read()
            failed.append(data)
            ParseJson('dumps/failed_dumps.json').write(failed)
            print("Failed to insert data")

    def insert_many(self, data):
        self._collection.insert_many(data)

    def find(self, query):
        return self._collection.find(query)

    def set_collection(self, collection):
        self._collection = self._db[collection]

    def set_database(self, database):
        self._db = self.mongo_client[database]
