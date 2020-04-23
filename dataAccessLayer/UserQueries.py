from dataAccessLayer.interfaces.IUserQueries import IUserQueries
import pandas as pd
from helpers import helpers
from entities.User import User

class UserQueries(IUserQueries):
    def __init__(self):
        self.users_df = pd.read_csv("dataAccessLayer/data/users.csv") 
        pass

    def get_user_query(self, _id):
        signle_user = self.users_df.loc[self.users_df['id'] == _id]
        userDict = helpers.rowToJson(signle_user)
        userEntity = User.from_dict(userDict)
        return userEntity

    def get_users_query(self):
        all_users = self.users_df
        all_users_arr = helpers.dfToArrayOfJsonWithoutIdx(all_users)
        Users = []
        for user in all_users_arr:
            Users.append(User.from_dict(user))
        return Users



