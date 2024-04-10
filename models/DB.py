import pymongo as db
from bson.objectid import ObjectId

class DBMongo():
    def __init__(self,ip = "127.0.0.1",port = 27017):
        #Todo  Check DB connection or not 
        self.ip = ip
        self.port = port
      
        pass

    
    def Connect_DB(self,DBName,TableName):
        
        try: 
            
            maxSevSelDelay = 100
            self.myclient = db.MongoClient("mongodb://{0}:{1}".format(self.ip,self.port)
                                           , serverSelectionTimeoutMS=maxSevSelDelay)
            
            server_info  =  self.myclient.server_info()
            
            print (server_info)
            
            self._db = self.myclient[DBName][TableName]      
            print("Connecting to")
            return True         
            
        except Exception as e:
            print("Error =  " + str(e))
                 
            return  False
        
        
     
    def insert_one(self,data):
        result = self._db.insert_one(data)
        return result
     
    def  update_one(self,Newdata,id):
        filter = {'_id': ObjectId(id)}
        newvalues = {"$set": Newdata }
        self._db.update_one(filter,newvalues)
    def delete_one(self,id):
        filter = {'_id': ObjectId(id)}
        self._db.delete_one(filter)
        
    def find(self,fillter):
        result = self._db.find(fillter)   
        return  result
    
    def findAll(self):
        result = self._db.find()   
        return  result
    
    def Disconnect(self):
        try:
            self.myclient.close()
        except Exception as e:
            print("Error =  " + str(e))