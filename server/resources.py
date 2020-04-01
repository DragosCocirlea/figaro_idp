from flask_restful import Resource
from flask import request
from models import UserModel, BarbershopModel, BarberModel, ServiceModel, AppointmentModel
import sys


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
            if user is None: # add user
                user = UserModel(req_json)
                user.save_to_db()
                return {'msg' : 'User {} has been succesfully added to the db'.format(user_email)}, 200
            else: # update user
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



        return {'msg' : 'S-a facut get pe appointment', 'json' : req_json}

    def post(self):
        req_json = request.get_json()
        return {'msg' : 'S-a facut post pe appointment', 'json' : req_json}
    
    def delete(self):
        req_json = request.get_json()
        return {'msg' : 'S-a facut delete pe appointment', 'json' : req_json}


class BarbershopData(Resource):
    def get(self):
        req_json = request.get_json()
        return {'msg' : 'S-a facut get pe barbershops', 'json' : req_json}


class BarberData(Resource):
    def get(self):
        req_json = request.get_json()
        return {'msg' : 'S-a facut get pe barbers', 'json' : req_json}


class ServiceData(Resource):
    def get(self):
        req_json = request.get_json()
        return {'msg' : 'S-a facut get pe services', 'json' : req_json}