from mongoengine import Document
from mongoengine.fields import StringField, BooleanField

class Subscriber(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone = StringField()
    email_send = BooleanField(default=False)
    sms_send = BooleanField(default=False)