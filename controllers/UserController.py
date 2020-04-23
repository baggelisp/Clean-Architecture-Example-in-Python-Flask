from flask import jsonify

from service.interfaces.IUserService import IUserService
from .interfaces.IUserController import IUserController

class UserController(IUserController):
    def __init__(self, user_service: IUserService):
        self.user_service = user_service

    def get_user_controller(self, _id):
        print ('User controller')
        User =  self.user_service.get_user_service(_id)
        return jsonify(User.to_dict())

    
    def get_all_user_controller(self):
        Users =  self.user_service.get_users_service()
        repsArrayOfUsers = list(map(lambda x: x.__dict__, Users)6)
        return jsonify(users=repsArrayOfUsers) 

