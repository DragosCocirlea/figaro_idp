import json
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from math import floor, inf
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db:3306/figaro' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.app_context().push()
db = SQLAlchemy(app)


############################################################# ADMIN FUNCTIONS #############################################################
@app.route('/admin/add_barbershop', methods=['POST'])
def add_barbershop():
    print(request.get_json())
    bbs = Barbershop(json.loads(request.get_json()))
    db.session.add(bbs)
    db.session.commit()
    return json.dumps({'Response':'Successfully added\n'})

############################################################## OVERVIEW ##############################################################
@app.route('/barbershops')
def show_barbershops():
    columns = ['id', 'name', 'address', 'rating', 'coordX', 'coordY']
    barbershops = []
    for bbs in Barbershop.query.all():
        barbershops.append([bbs.id, bbs.name, bbs.address, str(bbs.rating), str(bbs.coordX), str(bbs.coordY)])
    return render_template('table.html', records=barbershops, colnames=columns, tablename='BARBERSHOPS', size=len(columns))

@app.route('/barbers')
def show_barbers():
    columns = ['id', 'name', 'rating', 'bbs_id']
    barbers = []
    for barber in Barber.query.all():
        barbers.append([barber.id, barber.name, str(barber.rating), barber.bbs_id])
    return render_template('table.html', records=barbers, colnames=columns, tablename='BARBERS', size=len(columns))

@app.route('/clients')
def show_clients():
    columns = ['id', 'name', 'phone', 'sex', 'birthday', 'rating']
    clients = []
    for client in Client.query.all():
        clients.append([client.id, client.name, client.phone, client.sex, str(client.birthday), str(client.rating)])
    return render_template('table.html', records=clients, colnames=columns, tablename='CLIENTS', size=len(columns))

@app.route('/services')
def show_services():
    columns = ['id', 'name', 'price', 'bbs_id']
    services = []
    for serv in Service.query.all():
        services.append([serv.id, serv.name, str(serv.price), serv.bbs_id])
    return render_template('table.html', records=services, colnames=columns, tablename='SERVICES', size=len(columns))

@app.route('/appointments')
def show_appointments():
    columns = ['id', 'date', 'time', 'barber_id', 'client_id', 'service_id']
    appointments = []
    for app in Appointment.query.all():
        appointments.append([app.id, app.date, app.time, app.barber_id, app.client_id, app.service_id])
    return render_template('table.html', records=appointments, colnames=columns, tablename='APPOINTMENTS', size=len(columns))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
