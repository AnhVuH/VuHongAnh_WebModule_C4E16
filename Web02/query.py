from models.service import Service
import mlab

mlab.connect()

#take all documents
all_services = Service.objects()

# print(all_services[0]['name'])
print(all_services[2].name)
