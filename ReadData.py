import pymongo as db
from PIL import Image
from io import BytesIO
myclient = db.MongoClient("mongodb://localhost:27017")
# * Note: Connect mydatabase
mydb = myclient["local"]
stock = mydb["Stock"]
mydoc = stock.find_one()
imgData = mydoc["Image"]
imgQr = mydoc["qr"]
im = Image.open(BytesIO(imgData))
im.save('./temp/output/img.jpg')
imQr = Image.open(BytesIO(imgQr))
imQr.save('./temp/output/imgQr.jpg')

