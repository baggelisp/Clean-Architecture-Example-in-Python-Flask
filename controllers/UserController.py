from flask import jsonify

from service.interfaces.IUserService import IUserService
from .interfaces.IUserController import IUserController

class UserController(IUserController):
    def __init__(self, user_service: IUserService):
        self.user_service = user_service

    def get_user_controller(self, _id):
        print ('User controller')
        User =  self.user_service.get_user_service(_id) # returns entity
        return jsonify(User.to_dict()) # entity to object

    
    def get_all_user_controller(self):
        print ('User controller')
        Users =  self.user_service.get_users_service() # returns list of entities
        repsArrayOfUsers = list(map(lambda x: x.__dict__, Users)) # list of entities to list of objects 
        return jsonify(users=repsArrayOfUsers) 

