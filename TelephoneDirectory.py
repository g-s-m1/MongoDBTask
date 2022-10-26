import pymongo

mongo=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db=mongo['guvi3']  # database
mycollection=db['teledir'] #collection
contact_information=[{'name':'Rachel','phone':'7896541233','place':'Pune'},
                     {'name':'Monica','phone':'9052147896','place':'Kolkata'},
                     {'name':'Ross','phone':'9632587412','place':'Chennai'},
                     {'name':'Phoebe','phone':'9296541233','place':'Kochi'},
                     {'name':'Joey','phone':'9452147896','place':'Banglore'},
                     {'name':'Joey','phone':'9452145696','place':'Palakkad'},
                     {'name':'Chandler','phone':'9632567412','place':'Hyderabad'}]

mycollection.insert_many(contact_information) #insert query

data=mycollection.find() #show the records
for dat in data:
    print(dat)

query={'name':'Joey'}
update={"$set":{'name':'Joseph'}}
db.mycollection.update_one(query,update) #update query
data1=mycollection.find()
for dat1 in data1:
    print(dat1)

query1={'name':'Joseph'}
db.mycollection.delete_one(query1) #delete query
data2=mycollection.find()
for dat2 in data2:
    print(dat2)
