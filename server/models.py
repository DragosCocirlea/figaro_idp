from server import db

class Barbershop(db.Model):
    __tablename__ = 'Barbershops'
    id = db.Column('id', db.String, primary_key = True)
    name = db.Column('name', db.String)
    address = db.Column('address', db.String)
    rating = db.Column('rating', db.Float)
    coordX = db.Column('coordX', db.Float)
    coordY = db.Column('coordY', db.Float)

    def __init__(self, json_bbs):
        self.id = json_bbs['id']
        self.name = json_bbs['name']
        self.address = json_bbs['address']
        self.rating = json_bbs['rating']
        self.coordX = json_bbs['coordX']
        self.coordY = json_bbs['coordY']

class Barber(db.Model):
    __tablename__ = 'Barbers'
    id = db.Column('id', db.String, primary_key = True)
    name = db.Column('name', db.String)
    rating = db.Column('rating', db.Float)
    bbs_id = db.Column('bbs_id', db.String, db.ForeignKey('Barbershops.id'))

    def __init__(self, json_barber):
        self.id = json_barber['id']
        self.name = json_barber['name']
        self.rating = json_barber['rating']
        self.bbs_id = json_barber['bbs_id']

class Client(db.Model):
    __tablename__ = 'Clients'
    id = db.Column('id', db.String, primary_key = True)
    name = db.Column('name', db.String)
    phone = db.Column('phone', db.String)
    sex = db.Column('sex', db.String)
    birthday = db.Column('birthday', db.Date)
    rating = db.Column('rating', db.Float)

    def __init__(self, json_client):
        self.id = json_client['id']
        self.name = json_client['name']
        self.phone = json_client['phone']
        self.sex = json_client['sex']
        # self.birthday = json_client['birthday']
        self.rating = json_client['rating']

class Service(db.Model):
    __tablename__ = 'Services'
    id = db.Column('id', db.String, primary_key = True)
    name = db.Column('name', db.String)
    price = db.Column('price', db.Integer)
    bbs_id = db.Column('bbs_id', db.String, db.ForeignKey('Barbershops.id'))

    def __init__(self, json_service):
        self.id = json_service['id']
        self.name = json_service['name']
        self.price = json_service['price']
        self.bbs_id = json_service['bbs_id']

class Appointment(db.Model):
    __tablename__ = 'Appointments'
    id = db.Column('id', db.String, primary_key = True)
    date = db.Column('date', db.String)
    time = db.Column('time', db.String)
    barber_id = db.Column('barber_id', db.String, db.ForeignKey('Barbers.id'))
    client_id = db.Column('client_id', db.String, db.ForeignKey('Clients.id'))
    service_id = db.Column('service_id', db.String, db.ForeignKey('Services.id'))

    def __init__(self, json_appointment):
        self.id = json_appointment['id']
        self.date = json_appointment['name']
        self.time = json_appointment['price']
        self.barber_id = json_appointment['barber_id']
        self.client_id = json_appointment['client_id']
        self.service_id = json_appointment['service_id']