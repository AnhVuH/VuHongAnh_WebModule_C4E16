from models.customer import Customer
from mlab import connect
from random import randint, choice
from faker import Faker
import sys
sys.path.append("E:\C4E16\WebModule\Web02\mlab.py")

connect()
fake = Faker()

for i in range(100):
    print('Saving customer', i+1,'....')
    new_customer = Customer(name = fake.name(),
                                    gender = randint(0,1),
                                    email = fake.email(),
                                    phone = fake.phone_number(),
                                    job = fake.job(),
                                    company = fake.company(),
                                    contacted = choice([True,False]))

    new_customer.save()
