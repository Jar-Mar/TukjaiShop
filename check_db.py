import pymongo as db
myclient = db.MongoClient("mongodb://localhost:27017")
# * Note: Connect mydatabase
mydb = myclient["local"]
print(myclient.list_database_names())

# * Use for create collections
#mydb.create_collection("venders")
mycol = mydb["venders"]





Vendor = {"Name":"A","Tel":"0649859632","Localtion":"N/A"}

myquery = { "Name": "A" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
result = bool(mydoc)

myquery2 = { "Name": "C" }
mydoc2 = mycol.find(myquery2)
result2 = bool(mydoc2)
print (mydoc.retrieved)
print (mydoc2.retrieved)
# * Check Name Vendor before insert
# result = mycol.insert_one(Vendor)