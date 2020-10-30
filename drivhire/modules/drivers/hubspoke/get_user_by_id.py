from drivhire.modules.drivers.schema.user import Driver


def get_user_by_id(user_id):
    try:
        user = Driver.objects(id=user_id).first()
        return user.to_dict()
    except Exception as err:
        raise Exception(err)
