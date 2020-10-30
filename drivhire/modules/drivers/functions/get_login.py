from drivhire.modules.drivers.schema.user import Driver
from drivhire.modules.utils.send_sms import send_sms
from drivhire.modules.utils.generate_otp import generate_otp
from drivhire.modules.utils.create_redis_session import  create_redis_session
from drivhire.modules.utils.access_token import create_access_token

def get_login(req):
    try:
        user = Driver.objects(phone=req.phone).first()
        otp = generate_otp()
        message = " Your Otp is : "+otp
        if user:
            user.otp = otp
            user.save()
            session_id = create_redis_session(user.id)
            data = {'sub':{
                'user_id':session_id,
                'valid':True
            }}
            access_token = create_access_token(data)
            # send_sms(message, user.phone)
            return {"statusCode":201, "message":"Otp has been sent to the registered phone number","data":{"access_token":access_token}}
        else:
            new_user = Driver(phone=req.phone, otp=otp).save()
            session_id = create_redis_session(user.id)
            data = {'sub':{
                'user_id':session_id,
                'valid':True
            }}
            access_token = create_access_token(data)
            # send_sms(message, req.phone)
            return {"statusCode":201, "message":"user created and sent a otp to the phone number","data":{"access_token":access_token}}



    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
