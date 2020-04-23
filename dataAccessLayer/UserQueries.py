from dataAccessLayer.interfaces.IUserQueries import IUserQueries

class UserQueries(IUserQueries):
    def __init__(self):
        pass

    def get_user_query(self, _id):
        print ('User data access')

        return 'baggelos'
