from mongoengine import Document, IntField, StringField, BooleanField, URLField, ListField

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = URLField()
    description = StringField()
    measurements = ListField()
