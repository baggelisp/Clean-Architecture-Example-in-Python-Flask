from service.interfaces.IUserService import IUserService
from dataAccessLayer.interfaces.IUserQueries import IUserQueries


class UserService(IUserService):
    def __init__(self, query_manager: IUserQueries):
        self.query_manager = query_manager

    def get_user_service(self, _id):
        print ('User services')
        user = self.query_manager.get_user_query(_id)
        return user
