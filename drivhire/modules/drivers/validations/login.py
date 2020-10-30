from pydantic import BaseModel


class DriverLogin(BaseModel):
    phone: str
