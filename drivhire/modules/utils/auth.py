from fastapi import Depends
from fastapi.security.http import HTTPBearer, HTTPBasicCredentials
import jwt
import os
from drivhire.conn.redis import conn
from drivhire.modules.drivers.hubspoke.get_user_by_id import get_user_by_id

auth = HTTPBearer()

def decrypt_token(token: str):
    payload = jwt.decode(token, os.environ.get('SECRET_KEY'),'HS256')
    return payload

def get_current_user(session_id):
    user_session = conn.hgetall(session_id)
    print(user_session)
    if user_session[b'valid']== b'True':
        user_id = user_session[b'userid'].decode('utf-8')
        user = get_user_by_id(user_id)
        if user:
            return user
        else:
            return False


async def auth_scheme(token: HTTPBasicCredentials = Depends(auth)):
    token = token.credentials
    payload = decrypt_token(token)
    print(payload['sub']['user_id'])
    current_user = get_current_user(payload['sub']['user_id'])
    return current_user
