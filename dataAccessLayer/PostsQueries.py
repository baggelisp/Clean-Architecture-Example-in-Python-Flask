from dataAccessLayer.interfaces.IPostsQueries import IPostsQueries
import pandas as pd
from dataAccessLayer.helpers.CommonUsed import CommonUsed
from entities.Post import Post

class PostsQueries(IPostsQueries):
    def __init__(self):
        self.posts_df = pd.read_csv("dataAccessLayer/data/posts.csv") 

    def get_single_post_query(self, _id):
        signle_post = self.posts_df.loc[self.posts_df['id'] == _id]
        postDict = CommonUsed.rowToJson(signle_post)
        postEntity = Post(postDict['id'],postDict['userId'],postDict['title'],postDict['body'])
        return postEntity # returns entity

    def get_all_posts_query(self):
        allPostsDict = CommonUsed.dfToArrayOfJsonWithoutIdx(self.posts_df)
        Posts = []
        for post in allPostsDict:
            Posts.append(Post(postDict['id'],postDict['userId'],postDict['title'],postDict['body']))
        return Posts # returns array of entities
