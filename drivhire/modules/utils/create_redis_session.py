from drivhire.conn.redis import conn
import uuid
from datetime import datetime

def create_redis_session(user_id):
    try:
        id = str(uuid.uuid1())
        info = {"sessionId": id, "valid":"True","userid":str(user_id),"timestamp":str(datetime.now())}
        conn.hmset(id,info)
        return id
    except Exception as err:
        raise Exception(err)
