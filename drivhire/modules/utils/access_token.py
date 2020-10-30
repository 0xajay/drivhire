import jwt
from datetime import datetime, timedelta
import os

def create_access_token(data: dict):
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=30)
        to_encode.update({"exp":expire})
        encoded_jwt = jwt.encode(to_encode, os.environ.get('SECRET_KEY'), 'HS256')
        return encoded_jwt
    except Exception as err:
        raise Exception(err)
