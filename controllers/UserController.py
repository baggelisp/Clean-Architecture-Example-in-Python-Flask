
from service.interfaces.IUserService import IUserService
from .interfaces.IUserController import IUserController

class UserController(IUserController):
    def __init__(self, user_service: IUserService):
        self.user_service = user_service

    def get_user_controller(self, _id):
        print ('User controller')
        user =  self.user_service.get_user_service(_id)
        return user

