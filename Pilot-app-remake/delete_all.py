from models.service import Service
import mlab

mlab.connect()

all_services = Service.objects()
all_services.delete()
