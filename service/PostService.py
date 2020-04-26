from service.interfaces.IPostService import IPostService
from dataAccessLayer.interfaces.IPostsQueries import IPostsQueries
from dataAccessLayer.interfaces.ICommentsQueries import ICommentsQueries


class PostService(IPostService):
    def __init__(self, posts_query_manager: IPostsQueries, comments_query_manager: ICommentsQueries):
        self.posts_query_manager = posts_query_manager
        self.comments_query_manager = comments_query_manager

    def get_single_post_service(self, _id):
        print ('Post services')
        Post = self.posts_query_manager.get_single_post_query(_id) 
        return Post # returns post entity

    def get_single_post_comments_service(self, _id):
        print ('Post services')
        Post = self.posts_query_manager.get_single_post_query(_id) # returns post entity
        commentsEntitiesArr = self.comments_query_manager.get_comment_of_single_post(_id) # returns array of entities
        # List of entities to list of objects
        commentsArray = list(map(lambda x: x.__dict__, commentsEntitiesArr))
        # populate post with commnets
        setattr(Post, 'comments', commentsArray)
        return Post  # returns post entity

