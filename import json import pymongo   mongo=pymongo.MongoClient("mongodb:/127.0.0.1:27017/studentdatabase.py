import json
import pymongo
 
mongo=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db=mongo['student8']  # database
mycollection=db['std8'] #collection
collection7=db['std7']
collection6=db['std6']
data = [json.loads(line)
        for line in open('students.json', 'r', encoding='utf-8')]
mycollection.insert_many(data) #insert query
db.mycollection.find({"scores":{"score":{'$lt' : 40}}},{"name":1,"_id":0,"scores":0});#qn2
db.mycollection.find({"fail":{"score":{'$lt' : 40}},"scores":{"pass":{'$gte' : 40}}});#qn3
collection6.insert_many(db.mycollection.find({"scores":{"score":{'$lt' : 40}}}))#qn6
collection7.insert_many(db.mycollection.find({"scores":{"score":{'$gte' : 40}}}))#qn7
