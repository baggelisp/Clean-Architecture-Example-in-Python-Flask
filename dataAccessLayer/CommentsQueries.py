from dataAccessLayer.interfaces.ICommentsQueries import ICommentsQueries
import pandas as pd
from helpers import helpers
from entities.Comment import Comment

class CommentsQueries(ICommentsQueries):
    def __init__(self):
        self.comments_df = pd.read_csv("dataAccessLayer/data/comments.csv") 
        pass

    def get_comment_of_single_post(self, post_id):
        signle_post_comments = self.comments_df.loc[self.comments_df['postId'] == post_id]
        commentsArr = helpers.dfToArrayOfJsonWithoutIdx(signle_post_comments)
        commentsEntitiesArr = []
        for comment in commentsArr:
            commnetEntity = Comment(comment['id'], comment['postId'], comment['name'], comment['body'])
            # return dictionare
            # commentsEntitiesArr.append(commnetEntity.to_dict())
            # or return entity
            commentsEntitiesArr.append(commnetEntity)
        return commentsEntitiesArr
