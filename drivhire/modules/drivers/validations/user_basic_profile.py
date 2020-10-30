from pydantic import BaseModel


class DriverBasicProfile(BaseModel):
    first_name : str
    last_name  : str
    email : str
    profile_pic : str = None
