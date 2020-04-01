from flask_restful import Resource
from flask import request
from sqlalchemy.sql import text
from models import UserModel, BarbershopModel, BarberModel, ServiceModel, AppointmentModel
import geopy.distance

class UserData(Resource):
    def get(self):
        user_email = request.get_json()['email']
        try:
            user = UserModel.query.filter_by(id = user_email).first()
            return user.to_json(), 200
        except:
            return {'msg' : 'Couldn\'t get user from server db'}, 500


    def post(self):
        req_json = request.get_json()
        user_email = req_json['email']
        try:
            user = UserModel.query.filter_by(id = user_email).first()
            if user is None:
                user = UserModel(req_json)
                user.save_to_db()
                return {'msg' : 'User {} has been succesfully added to the db'.format(user_email)}, 200
            else:
                user.update_in_db(req_json)
                return {'msg' : 'User {} has been succesfully updated in the db'.format(user_email)}, 200
        except:
            return {'msg' : 'Couldn\'t add or update user in the server db'}, 500


    def delete(self):
        user_email = request.get_json()['email']
        try:
            appointments = AppointmentModel.query.filter_by(client_id = user_email).all()
            for appointment in appointments:
                appointment.delete_from_db()
            user = UserModel.query.filter_by(id = user_email).first()
            user.delete_from_db()
            return {'msg' : 'User {} has been succesfully deleted'.format(user_email)}, 200
        except:
            return {'msg' : 'Couldn\'t add or update user in the server db'}, 500
            


class AppointmentData(Resource):
    def get(self):
        user_email = request.get_json()['email']
        appointments_json = []

        appointments = AppointmentModel.query.filter_by(client_id = user_email).all()
        for appointment in appointments:
            appointments_json.append(appointment.to_json())

        return appointments_json

    def post(self):
        req_json = request.get_json()
        # TODO: implement making an appointment
        return {'msg' : 'S-a facut post pe appointment', 'json' : req_json}
    
    def delete(self):
        req_json = request.get_json()
        appointment_id = req_json['appointment_id']

        appointment = AppointmentModel.query.filter_by(id = appointment_id).first()
        if appointment is None:
            return {'msg' : 'This appointment doesn\'t exist'}
        else:
            appointment.delete_from_db()
            return {'msg' : 'Appointment succesfully deleted'}


class BarbershopData(Resource):
    def get(self):
        req_json = request.get_json()
        criteria = req_json['criteria']
        coordX = req_json['coordX']
        coordY = req_json['coordY']

        if criteria == 'default':
            barbershops = BarbershopModel.query.all()
        elif criteria == 'name':
            search = '%{}%'.format(req_json['name'])
            barbershops = BarbershopModel.query.filter(BarbershopModel.name.ilike(search)).all()
        elif criteria == 'rating':
            barbershops = BarbershopModel.query.order_by(BarbershopModel.rating.desc()).all()
        elif criteria == 'distance':
            order_by_string = 'abs(coordX - {}) + abs(coordY - {})'.format(coordX, coordY)
            barbershops = BarbershopModel.query.order_by(text(order_by_string)).all()
        else:
            return 'Bad search criteria', 400

        barbershops_json = []
        for barbershop in barbershops:
            json = barbershop.to_json()
            distance = geopy.distance.vincenty((coordX, coordY), (json['coordX'], json['coordY'])).km
            json['distance'] = distance
            barbershops_json.append(json)

        return barbershops_json

class BarberData(Resource):
    def get(self):
        barbershop_id = request.get_json()['bbs_id']
        barbers_json = []
        barbers = BarberModel.query.filter_by(bbs_id = barbershop_id).all()
        for barber in barbers:
            barbers_json.append(barber.to_json())
        return barbers_json

class ServiceData(Resource):
    def get(self):
        barbershop_id = request.get_json()['bbs_id']
        services_json = []
        services = ServiceModel.query.filter_by(bbs_id = barbershop_id).all()
        for service in services:
            services_json.append(service.to_json())
        return services_json