from pymongo import MongoClient

uri = 'mongodb://admin:123456@ds117489.mlab.com:17489/aboco1'

client = MongoClient(uri)

db = client.get_default_database()

users = db['users']

list_users=[
        {
        'username': 'tuananh',
        'name' : 'Huynh Tuan Anh',
        'gender': 'Male',
        'age' : 22,
        'hobbies':'......'
        },
        {
        'username': 'quy',
        'name' : 'Dinh Cong Quy',
        'gender': 'Male',
        'age' : 20,
        'hobbies':'......'
        },
        {
        'username': 'honganh',
        'name' : 'Vu Hong Anh',
        'gender': 'Female',
        'age' : 29,
        'hobbies':'Film Photography, Bicyling, Martial Art, Reading book'
        },
        ]
users.insert_many([user for user in list_users])
