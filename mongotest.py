import pymongo

client = pymongo.MongoClient("mongodb+srv://shashank:mongodb123@cluster0.hzvgv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "shashank",
    "email" : "shashank@ineuron.ai",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)