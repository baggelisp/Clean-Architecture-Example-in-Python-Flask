from dataAccessLayer.interfaces.IPostsQueries import IPostsQueries
import pandas as pd
from helpers import helpers
from entities.Post import Post

class PostsQueries(IPostsQueries):
    def __init__(self):
        self.posts_df = pd.read_csv("dataAccessLayer/data/posts.csv") 
        pass

    def get_single_post_query(self, _id):
        signle_post = self.posts_df.loc[self.posts_df['id'] == _id]
        postDict = helpers.rowToJson(signle_post)
        postEntity = Post(postDict['id'],postDict['userId'],postDict['title'],postDict['body'])
        return postEntity

    def get_all_posts_query(self):
        """
        """

        raise NotImplementedError
