from fastapi import APIRouter, Depends
from drivhire.modules.drivers.validations.login import DriverLogin
from drivhire.modules.drivers.validations.user_basic_profile import DriverBasicProfile
from drivhire.modules.drivers.functions.get_login import get_login
from drivhire.modules.drivers.functions.create_driver_profile import create_driver_profile
from drivhire.modules.utils.auth import auth_scheme
from fastapi.security.http import HTTPBearer, HTTPBasicCredentials

router = APIRouter()


@router.post("/driver")
async def create_driver(login: DriverLogin):
    try:
        result = get_login(login)
        return result
    except Exception as err:
        return {"statusCode":400, "message":str(err)},400


@router.post("/driver/basic-profile")
async def driver_profile(req: DriverBasicProfile, current_user: dict = Depends(auth_scheme)):
    try:
        if current_user:
            result = create_driver_profile(req, current_user)
            return result
        else:
            return {"statusCode":401, "message":"you are not authorized to use this route"},401
    except Exception as err:
        return {"statusCode":400, "message":str(err)},400
