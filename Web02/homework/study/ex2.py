from mongoengine import *

# mongodb://<dbuser>:<dbpassword>@ds129946.mlab.com:29946/muadongkhonglanh

db = 'muadongkhonglanh'
user = 'admin'
password = '123456'
host = 'ds129946.mlab.com'
port = 29946

connect(db, username = user, password = password,host = host, port = port)

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0:Female , 1: Male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

all_services= Service.objects()


# id_to_find =  "5ac0c3c81c0dea21ac0b6502"
id_to_find =  "5ac0c3c91c0dea21ac0b6503"

 # a list with one document which its id is id_to_find
print(all_services(id = id_to_find).to_json())
print(all_services(id__exact = id_to_find).to_json())

# a document which its id is id_to_find
print(all_services.get(id = id_to_find).to_json())
print(all_services.get(id__exact = id_to_find).to_json())
