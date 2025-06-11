from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app import models, schemas
from app.database import AsyncSessionLocal, engine, Base

app = FastAPI()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.post("/teams/", response_model=schemas.Team)
async def create_team(instructor: schemas.TeamCreate, db: AsyncSession = Depends(get_db)):
    db_team = models.Team(**instructor.dict())
    db.add(db_team)
    await db.commit()
    await db.refresh(db_team)
    return db_team

@app.get("/teams/", response_model=List[schemas.Team])
async def read_teams(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):    
    result = await db.execute(select(models.Team).offset(skip).limit(limit))
    teams = result.scalars().all()
    return teams

@app.get("/teams/{teams_id}", response_model=schemas.Team)
async def read_team(team_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Team).where(models.Team.id == team_id))
    team = result.scalars().first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.put("/teams/{teams_id}", response_model=schemas.Team)
async def update_team(
    team_id: int, 
    team: schemas.TeamCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(models.Team).where(models.Team.id == team_id))
    db_team = result.scalars().first()
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    
    for key, value in team.dict().items():
        setattr(db_team, key, value)
    
    await db.commit()
    await db.refresh(db_team)
    return db_team

@app.delete("/teams/{teams_id}")
async def delete_team(teams_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Team).where(models.Team.id == teams_id))
    db_team = result.scalars().first()
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    
    await db.delete(db_team)
    await db.commit()
    return {"message": "Team deleted successfully"}

@app.post("/drivers/", response_model=schemas.Driver)
async def create_driver(student: schemas.DriverCreate, db: AsyncSession = Depends(get_db)):
    db_driver = models.Driver(**student.dict())
    db.add(db_driver)
    await db.commit()
    await db.refresh(db_driver)
    return db_driver

@app.get("/drivers/", response_model=List[schemas.Driver])
async def read_drivers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).offset(skip).limit(limit))
    drivers = result.scalars().all()
    return drivers

@app.get("/drivers/{drivers_id}", response_model=schemas.Driver)
async def read_driver(driver_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).where(models.Driver.id == driver_id))
    driver = result.scalars().first()
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@app.put("/drivers/{drivers_id}", response_model=schemas.Driver)
async def update_driver(
    driver_id: int,
    driver: schemas.DriverCreate, 
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(models.Driver).where(models.Driver.id == driver_id))
    db_driver = result.scalars().first()
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    
    for key, value in driver.dict().items():
        setattr(db_driver, key, value)
    
    await db.commit()
    await db.refresh(db_driver)
    return db_driver

@app.delete("/drivers/{drivers_id}")
async def delete_driver(driver_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).where(models.Driver.id == driver_idr))
    db_driver = result.scalars().first()
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    
    await db.delete(db_driver)
    await db.commit()
    return {"message": "Driver deleted successfully"}

@app.get("/teams/{teans_id}/drivers/", response_model=List[schemas.Driver])
async def read_drivers_by_teams(teams_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(models.Driver).where(models.Driver.team_id == teams_id)
    )
    drivers = result.scalars().all()
    return drivers