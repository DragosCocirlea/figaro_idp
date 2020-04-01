from models import *

barbershops = [
    {'name' : 'Vagabond Hair Studio', 'address' : 'Bloc G1, Bulevardul Unirii 65, Bucuresti', 'coordX' : 44.426309, 'coordY' : 26.123891},
    {'name' : 'Office 21 Barbershop', 'address' : 'Strada Inginer Cristian Pascal 34, Bucuresti', 'coordX' : 44.450964, 'coordY' : 26.054762}
]

barbers = [
    {'name' : 'Ionutz', 'bbs_id' : 1},
    {'name' : 'Mihai', 'bbs_id' : 2}
]

services = [
    {'name' : 'Tuns modern', 'price' : 50, 'bbs_id' : 1},
    {'name' : 'Tuns cu ciobul', 'price' : 20, 'bbs_id' : 2}
]

def init_db_data():
    for bbs_json in barbershops:
        bbs = BarbershopModel(bbs_json)
        bbs.save_to_db()

    for b_json in barbers:
        b = BarberModel(b_json)
        b.save_to_db()

    for s_json in services:
        s = ServiceModel(s_json)
        s.save_to_db()
