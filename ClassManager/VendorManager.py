from pydantic import BaseModel 
from typing import Optional 

class Vendor(BaseModel):
    Name: str
    Tel: str
    Localtion: Optional[str] = "NA"

  