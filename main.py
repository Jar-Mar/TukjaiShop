from fastapi import FastAPI,Request,Response
from models.TukjaiData import Stock ,Vender
from pydantic import BaseModel
from models.DB import DBMongo
from bson.json_util import dumps
from fastapi.responses import JSONResponse
from bson.objectid import ObjectId
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str 
    price: float
    tax: float 


app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
    
#*Note Get Version 
@app.get("/")
def root():
    return {"message": "TUKJAISHOP API Version 0.0.1"} 



# use for create new item
@app.put("/goods/create")
async def create_new_goods(stock: Stock):   
#  Create new goods in databas
    try:
        data = stock.__dict__
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Stock")
        _id  =  mydb.insert_one(data)   
        data  = {'status': True , '_id' :str(_id.inserted_id)}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except  Exception as error: 
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")
        

# update item from Database
@app.put("/goods/update")
async def update_item(id:str,stock: Stock):
    try:
        data = stock.__dict__
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Stock")
        # filter = {'_id': ObjectId(id)}
        # # Values to be updated.
        # newvalues = { "$set": data }
        mydb.update_one(data,id)  
        data  = {'status': True , '_id' :id}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")


# delete item from Database
@app.delete("/goods/delete")
async def delete_item(id:str):
    try:
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Stock")
        mydb.delete_one(id) 
        result = mydb.findAll()
        data  = {'status': True , 'result' :result}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")

# use for checking good in stock
@app.get("/goods/instock")
async def instock():
    try:
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Stock")
        filter = { 'status': True ,"Qty": {"$gt": 0}}
        Result = mydb.find(filter)
        data = {"status": True,"result" : Result}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")
#region Images

# update item from Database
@app.put("/goods/updateImage")
async def update_image(id:str,image:str):
    try:
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Image")
        # Values to be updated.
        data = {'_id': ObjectId(id), 'image': image}
        mydb.insert_one(data)
        data = {"status": True,"_id" : id}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")
    
#endregion

    
#region Vendor
# use for create new Vendor
@app.put("/vender/create")
async def create_new_vendor(vendor: Vender):   
#  Create new goods in databas
    try:
        data = vendor.__dict__
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Vender")
        _id  =  mydb.insert_one(data)   
        data  = {'status': True , '_id' :str(_id.inserted_id)}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except  Exception as error: 
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")
    
# update Vendor from Database
@app.put("/vender/update")
async def update_Vender(id:str,vendr: Vender):
    try:
        data = vendr.__dict__
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Vender")
        # filter = {'_id': ObjectId(id)}
        # # Values to be updated.
        # newvalues = { "$set": data }
        mydb.update_one(data,id)  
        data  = {'status': True , '_id' :id}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")

@app.delete("/vender/delete")
async def delete_Vender(id:str):
    try:
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Vender")
        # filter = {'_id': ObjectId(id)}
        # # Values to be updated.
        # newvalues = { "$set": data }
        mydb.delete_one(id)  
        data  = {'status': True , '_id' :id}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")
    
@app.get("/vender/getAll")
async def get_all_vender():
    try:
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Vender")
        # filter = {'_id': ObjectId(id)}
        # # Values to be updated.
        # newvalues = { "$set": data }
        result =  mydb.findAll()  
        data  = {'status': True , 'result' :result}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")
    
@app.get("/vender/getOne")
async def get_one_vender(name:str):
    try:
        mydb = DBMongo()
        mydb.Connect_DB("TUKJAISHOP","Vender")
        filter = {'Name': name}
        result =  mydb.find(filter)  
        data  = {'status': True , 'result' :result}
        json = dumps(data)
        return Response(content=json, media_type="application/json")
    except Exception as error:  
        result = {"status": False , "message": str(error)}
        json = dumps(result)
        return Response(content = json , media_type="application/json")

#endregion

        
  
