from pydantic import BaseModel
from typing import Optional

class TeamBase(BaseModel):
    name: str
    age: int
    location: str
    image: Optional[bytes] = None 

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    
    class Config:
        from_attributes = True

class DriverBase(BaseModel):
    name: str
    age: int
    image: Optional[bytes] = None 
    team_id: int

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int
    
    class Config:
        from_attributes = True