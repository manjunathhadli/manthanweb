import pymongo
import time
from bson import ObjectId
import os

os.sys.path.append(os.environ['JALJAAL_HOME']+'/config')
import fbconfig

mongoclient = pymongo.MongoClient(fbconfig.prodhosts["mongodb1"])
print(mongoclient.list_database_names())
mongodb1 = mongoclient["mydatabase"]


allcollections = mongodb1.list_collection_names()


colheartbeat = mydb["heartbeat"]
colheartbeat.drop()

colheartbeat = mydb["joining"]
colheartbeat.drop()

print(mydb.list_collection_names())
