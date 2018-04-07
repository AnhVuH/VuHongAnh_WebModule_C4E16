from mongoengine import Document, StringField, IntField, BooleanField,URLField,ListField

# Create collection
# Design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0:Female , 1: Male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = URLField()
    description = StringField()
    measurements = ListField()

# class Customer(Document):
#     name = StringField()
#     gender = IntField()
#     email = StringField()
#     phone = StringField()
#     job = StringField()
#     company = StringField()
#     contacted = BooleanField()
