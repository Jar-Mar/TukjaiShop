import pymongo as db
from datetime import datetime
from uuid import uuid4
import qrcode
from PIL import Image
import io
myclient = db.MongoClient("mongodb://localhost:27017")
# * Note: Connect mydatabase
mydb = myclient["local"]
stock = mydb["Stock"]
def convert_image_bytes(img):
    img_byte = io.BytesIO()
    img.save(img_byte, format='JPEG')
    return img_byte.getvalue() 
# mydb.create_collection("Stock")

cost = 1000
price = cost * 1.65
data = {
    "vender": "A",
    "type": "table",
    "size": {
        "w": 100,
        "h": 100,
    },
    "Localtion": "N/A",
    "date" :"",
    "cost": cost,
    "price" :price,
}

d = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
eventid = str(d) + str(uuid4())+"_"+data["vender"]+'_'+data["type"]+"_"+str(data["cost"]) +"_"+str(data["price"])
data["_id"] = eventid 
data["datetime"] = d

# Create a QR code object with a larger size and higher error correction
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

# Add the data to the QR code object
qr.add_data(eventid)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("./temp/qr.jpg")



im = Image.open("./temp/qr.jpg")

img_good = Image.open("./temp/92667.jpg")
# image_bytes = io.BytesIO()
# im.save(image_bytes, format='JPEG')





data["qr"] = convert_image_bytes(im)
data["Image"] = convert_image_bytes(img_good)
result = stock.insert_one(data)

