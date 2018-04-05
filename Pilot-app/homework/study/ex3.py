from mongoengine import *

# mongodb://<dbuser>:<dbpassword>@ds129946.mlab.com:29946/muadongkhonglanh

db = 'muadongkhonglanh'
user = 'admin'
password = '123456'
host = 'ds129946.mlab.com'
port = 29946

connect(db, username = user, password = password,host = host, port = port)

class Person(DynamicDocument):
    meta = {'collection': 'service'}

all_services= Person.objects()


# id_to_del =  "5ac0c3c81c0dea21ac0b6502"
id_to_del =  "5ac0c3c91c0dea21ac0b6503"

all_services(id = id_to_del).delete()
