import datetime as dt
from fastapi import FastAPI
# from database import Base
from routes import trades
# from database import engine



app = FastAPI()
app.include_router(trades.router)



