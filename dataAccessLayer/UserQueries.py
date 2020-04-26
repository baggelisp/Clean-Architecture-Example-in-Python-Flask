from dataAccessLayer.interfaces.IUserQueries import IUserQueries
import pandas as pd
from dataAccessLayer.helpers.CommonUsed import CommonUsed
from entities.User import User


class UserQueries(IUserQueries):
    def __init__(self):
        self.users_df = pd.read_csv("dataAccessLayer/data/users.csv") 

    def get_user_query(self, _id):
        signle_user = self.users_df.loc[self.users_df['id'] == _id]
        userDict = CommonUsed.rowToJson(signle_user)
        userEntity = User.from_dict(userDict)
        return userEntity # returns entity

    def get_users_query(self):
        all_users = self.users_df
        all_users_arr = CommonUsed.dfToArrayOfJsonWithoutIdx(all_users)
        Users = []
        for user in all_users_arr:
            Users.append(User.from_dict(user))
        return Users # returns list of entities



