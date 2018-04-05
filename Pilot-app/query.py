from models.service import Service
import mlab

mlab.connect()

#take all documents
# all_services = Service.objects()

# print(all_services[0]['name'])
# print(all_services[2].name)
id_to_find ="5ac0c3c91c0dea21ac0b6503"

# Kevin = Service.objects(id = id_to_find)[0]
# Kevin = Service.objects.get(id = id_to_find)

service = Service.objects.with_id(id_to_find)

if service is None:
    print('Service not found')
else:
    # print(Kevin.to_mongo())
    # Kevin.delete()
    # print ("deleted")
    service.update(set__address='Trần Duy Hưng')
    service.reload()
    print(service.address)
