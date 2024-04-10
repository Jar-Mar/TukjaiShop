
from pydantic import BaseModel 
from typing import Optional 

class Vendors (BaseModel):
    IDs:str 
    Name: str 
    PhoneNumber: str 
    Address: str
    

class Sizes(BaseModel):
    Width: int 
    Length : int 
    Height : int 
    
'''
Date  is date input 
Sell Date is Date for Sell
Price ราคาขาย 
Cost  ต้นทุน

'''
class Stock (BaseModel):
    ID : str 
    Detail : str 
    VendorsIDs : str 
    Date : str 
    Costs : float 
    SellDate: float 
    Price :float
    # Size : Optional[Sizes] 
    # def __init__(self):
    #     self.Size = Sizes()
    #     self.ID = None
    #     self.Detail = None
    #     self.VendorsIDs = None
    #     self.Date = None
    #     self.Costs = None
    #     self.Price = None
        

   

    
