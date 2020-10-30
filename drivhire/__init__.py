from fastapi import FastAPI, Header, HTTPException, Depends
from mongoengine import connect
import os

app = FastAPI()
db = connect(host=os.environ.get('MONGO_URI'))


from drivhire.modules.drivers.routes import router as driver_routes


app.include_router(driver_routes, tags=["drivers"])
