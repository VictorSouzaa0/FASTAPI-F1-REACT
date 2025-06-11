from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from app.database import Base

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    location = Column(String)
    image = Column(LargeBinary)
    
    drivers = relationship("Driver", back_populates="team")

class Driver(Base):
    __tablename__ = "drivers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    image = Column(LargeBinary)
    team_id = Column(Integer, ForeignKey("teams.id"))
    
    team = relationship("Team", back_populates="drivers")