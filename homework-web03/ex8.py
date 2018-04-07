import ex7
from mongoengine import *

ex7.connect()
class River(DynamicDocument):
    meta = {"collection": "river"}

all_river_in_Africa = River.objects(continent= "Africa")

for river in all_river_in_Africa:
    print(river.to_json())
