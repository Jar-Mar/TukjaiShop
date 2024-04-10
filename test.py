
from ClassManager.ClassManager import  Vendors ,Stock
import json
from dataclasses import asdict

V1  =  Vendors (Name = "A",PhoneNumber = "0")
S = Stock ()


print (V1.Name)
print (json.dumps(asdict(S)))


