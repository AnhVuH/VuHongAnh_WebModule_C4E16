from models.service import Service
import mlab
from random import randint, choice
from faker import Faker

mlab.connect()

fake = Faker()
for i in range(100):
    print('Saving service', i+1,'....')
#Create a document
    new_service = Service(name = fake.name(), yob = randint(1995,2000), gender = randint(0,1), height = randint(150,180),
    phone = fake.phone_number(), address = fake.address(), status = choice([False, True]))
    new_service.save()

# print(fake.name())
# print(fake.address())
