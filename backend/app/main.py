from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from .database import AsyncSessionLocal,engine,Base
from fastapi.middleware.cors import CORSMiddleware
from . import schemas,models
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

#  @app.on_event("startup")
#  async def on_startup():
#      await init_db()

@app.get("/")
async def test():
    return {"message": "Test OK"}
    

@app.post("/teams/", response_model=schemas.Team)
async def create_team(team: schemas.TeamCreate, db: AsyncSession = Depends(get_db)):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    await db.commit()
    await db.refresh(db_team)
    return db_team

@app.get("/teams/", response_model=List[schemas.Team])
async def read_teams(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Team).offset(skip).limit(limit))
    teams = result.scalars().all()
    return teams

@app.get("/teams/{team_id}", response_model=schemas.Team)
async def read_team(team_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Team).where(models.Team.id == team_id))
    team = result.scalars().first()
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.put("/teams/{team_id}", response_model=schemas.Team)
async def update_team(team_id: int, team: schemas.TeamCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Team).where(models.Team.id == team_id))
    db_team = result.scalars().first()
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    for key, value in team.dict().items():
        setattr(db_team, key, value)
    await db.commit()
    await db.refresh(db_team)
    return db_team

@app.delete("/teams/{team_id}")
async def delete_team(team_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Team).where(models.Team.id == team_id))
    db_team = result.scalars().first()
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    await db.delete(db_team)
    await db.commit()
    return {"message": "Team deleted successfully"}

@app.post("/drivers/", response_model=schemas.Driver)
async def create_driver(driver: schemas.DriverCreate, db: AsyncSession = Depends(get_db)):
    db_driver = models.Driver(**driver.dict())
    db.add(db_driver)
    await db.commit()
    await db.refresh(db_driver)
    return db_driver

@app.get("/drivers/", response_model=List[schemas.Driver])
async def read_drivers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).offset(skip).limit(limit))
    drivers = result.scalars().all()
    return drivers

@app.get("/drivers/{driver_id}", response_model=schemas.Driver)
async def read_driver(driver_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).where(models.Driver.id == driver_id))
    driver = result.scalars().first()
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@app.put("/drivers/{driver_id}", response_model=schemas.Driver)
async def update_driver(driver_id: int, driver: schemas.DriverCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).where(models.Driver.id == driver_id))
    db_driver = result.scalars().first()
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    for key, value in driver.dict().items():
        setattr(db_driver, key, value)
    await db.commit()
    await db.refresh(db_driver)
    return db_driver

@app.delete("/drivers/{driver_id}")
async def delete_driver(driver_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).where(models.Driver.id == driver_id))
    db_driver = result.scalars().first()
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    await db.delete(db_driver)
    await db.commit()
    return {"message": "Driver deleted successfully"}

@app.get("/teams/{team_id}/drivers/", response_model=List[schemas.Driver])
async def read_drivers_by_team(team_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Driver).where(models.Driver.team_id == team_id))
    drivers = result.scalars().all()
    return drivers

if __name__ == "__main__":

    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1",port=8000, log_level="info", reload=True)