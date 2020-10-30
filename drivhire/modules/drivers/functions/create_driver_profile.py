from drivhire.modules.drivers.schema.user import Driver


def create_driver_profile(req, userdata):
    try:
        print(userdata["id"])
        user = Driver.objects(id=userdata["id"]).first()
        user.first_name = req.first_name
        user.last_name = req.last_name
        user.email = req.email.lower()
        user.profile_pic = req.profile_pic
        user.user_profile_created = True

        user.save()
        return {"statusCode":201, "message":"user basic profile created", "data":user.to_dict()},201
    except Exception as err:
        return {"statusCode":500, "message":str(err)},500
