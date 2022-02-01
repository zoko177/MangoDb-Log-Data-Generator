from pymongo import MongoClient
import mangoSetting


class Mangodb:
    def __init__(self):
        self.client = MongoClient(mangoSetting.MangoInfo().generate_link())
        self.db = self.client[mangoSetting.MangoInfo().db_name]
        self.structure_db = self.db["Structure"]
        self.generated_data_db = self.db["Generated Data"]

    def get_db(self):
        return self.db

    def get_structure(self):
        return self.db["Structure"].find_one({"_id": 1})

    def push_structure(self, new_st):
        self.structure_db.delete_many({})
        self.structure_db.insert_one(new_st)

    def push_data(self, data):
        self.generated_data_db.delete_many({})
        self.generated_data_db.insert_many(data)



