from pymodm import MongoModel, fields
from db import BaseDB

class PMData(MongoModel):
    pm10 = fields.IntegerField(mongo_name="pm10", min_value=1)
    pm25 = fields.IntegerField(mongo_name="pm25", min_value=1)
    pm100 = fields.IntegerField(mongo_name="pm100", min_value=1)
    temp = fields.IntegerField(mongo_name="temp", min_value=1)
    humidity = fields.IntegerField(mongo_name="humidity", min_value=1)
    # position = fields.CharField()
    date = fields.DateTimeField(mongo_name="date")
    class Meta():
        connection_alias = BaseDB.connectionAlias
    def clean(self):
       print("clean is performed")
