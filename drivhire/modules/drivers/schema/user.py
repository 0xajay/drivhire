from mongoengine import *
from datetime import datetime


class Driver(Document):
    first_name = StringField(required=False)
    last_name = StringField(required=False)
    phone = StringField(required=True)
    email = EmailField(required=False)
    profile_pic = StringField(required=False)
    otp = StringField(required=False)
    user_verified = BooleanField(required=True, default=False)
    user_created = BooleanField(required=True, default=False)
    user_profile_created = BooleanField(required=True, default=False)
    visibility = BooleanField(required=True, default=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.pk),
            "first_name":self.first_name,
            "last_name":self.last_name,
            "phone":self.phone,
            "email":self.email,
            "profile_pic":self.profile_pic,
            "otp":self.otp,
            "user_verified":self.user_verified,
            "user_created":self.user_created,
            "user_profile_created":self.user_profile_created,
            "visibility":self.visibility,
            "timestamp":self.timestamp
        }
