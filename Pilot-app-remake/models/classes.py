from mongoengine import Document, IntField, StringField, BooleanField, URLField, ListField, ReferenceField

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

class User(Document):
    username = StringField()
    password = StringField()
    email = StringField()
    fullname = StringField()

class Order(Document):
    service = ReferenceField(Service)
    user = ReferenceField(User)
    time_ordered = StringField()
    is_accepted = BooleanField()
