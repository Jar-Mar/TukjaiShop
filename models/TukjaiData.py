
from pydantic import BaseModel 





    
class Stock (BaseModel):
    status : bool
    Qty : int
    Type :str 
    Detail : str 
    VendorsIDs : str 
    Date : str 
    Costs : float 
    SellDate: float 
    Price :float
    Width: int 
    Length : int 
    Height : int 
    
class Vender (BaseModel):
    Name :str
    Tel : str 
    BankAccount : str
    BankName : str



    
    
    
  
    

   
        
