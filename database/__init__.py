from pymongo import MongoClient
from database.parse_json import ParseJson


class Database:
    def __init__(self, database="test", collection="test"):
        self.host = "localhost"

        self.port = 27017
        self.mongo_client = MongoClient(self.host, self.port, serverSelectionTimeoutMS=1000)
        self._db = self.mongo_client[database]
        self._collection = self._db[collection]

    def insert(self, data, path=""):
        file = 'dumps/'+path+'.json'

        failed_file ='dumps/'+path+'_failed_dumps.json'
        try:
            failed = ParseJson(failed_file).read()
            if len(failed) > 0:
                try:
                    self._collection.insert_many(failed)
                    ParseJson(failed_file).write([])
                    print("Failed dumps inserted")
                except:
                    print("Failed to insert failed dumps")

            self._collection.insert_one(data)

            read = ParseJson(file).read()
            read.append(data)
            ParseJson(file).write(read)
            print("Data inserted")
        except:
            failed = ParseJson(failed_file).read()
            failed.append(data)
            ParseJson(failed_file).write(failed)
            ParseJson(file).write(failed)
            print("Failed to insert data")

    def insert_many(self, data):
        self._collection.insert_many(data)

    def find(self, query):
        return self._collection.find(query)

    def set_collection(self, collection):
        self._collection = self._db[collection]

    def delete_data(self, collection: str):
        self._collection = self._db[collection]
        self._collection.drop()

    def set_database(self, database):
        self._db = self.mongo_client[database]

