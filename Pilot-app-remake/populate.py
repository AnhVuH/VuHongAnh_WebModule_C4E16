from models.service import Service
from mlab import connect

connect()

# new_service = Service(name = "Tú Linh", yob = 1994, gender = 0, height = 163,
#                     phone = "01696969696", address = "Hà Nội", status = False, image = "https://kenh14cdn.com/2018/4/3/27336457101555184300448656789127116148583231n-1522769154533543809313.jpg",
#                     description ="ngoan hiền, dễ thương, lễ phép với gia đình", measurements = [90,60,90])
# new_service = Service(name = "Trâm Anh", yob = 1995, gender = 0, height = 165,
#                     phone = "01696969789", address = "Hà Nội", status = False, image = "https://kenh14cdn.com/2018/4/3/120906dshotgirltramanh26-4d09d-15227687719141049112126.jpg",
#                     description ="ngoan hiền, dễ thương, lễ phép với gia đình", measurements = [90,60,90])
# new_service = Service(name = "Rocker Nguyễn", yob = 1993, gender = 1, height = 183,
#                     phone = "0123456789", address = "Sài Gòn", status = True, image = "http://sohanews.sohacdn.com/2016/14689720-1212672692111917-387201608-o-1476504322454.jpg",
#                     description ="ga lăng, dễ thương, chăm lo cho gia đình", measurements = [110,83,100])

new_service.save()
