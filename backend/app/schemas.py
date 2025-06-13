from pydantic import BaseModel
from typing import Optional

class TeamBase(BaseModel):
    name: str
    location: str
    image: Optional[str] = None 

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int
    
    class Config:
        from_attributes = True

class DriverBase(BaseModel):
    name: str
    age: int
    image: Optional[str] = None 
    team_id: int

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int
    
    class Config:
        from_attributes = True