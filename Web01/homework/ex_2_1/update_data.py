from pymongo import MongoClient

uri = 'mongodb://admin:123456@ds117489.mlab.com:17489/aboco1'

client = MongoClient(uri)

db = client.get_default_database()

users = db.users

new_user={
        'username':None ,
        'name' : None,
        'gender': None,
        'age' : None ,
        'hobbies':None}

for key in new_user:
    new_user[key] = input('Please enter {}: '.format(key))

if users.find_one({'username':new_user['username']}):
    users.replace_one({'username':new_user['username']},new_user)
else:
    users.insert_one(new_user)
