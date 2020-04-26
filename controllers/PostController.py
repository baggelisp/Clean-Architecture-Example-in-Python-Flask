from flask import jsonify

from service.interfaces.IPostService import IPostService
from .interfaces.IPostController import IPostController

class PostController(IPostController):
    def __init__(self, post_service: IPostService):
        self.post_service = post_service

    def get_single_post_controller(self, _id):
        print ('Post controller')
        Post =  self.post_service.get_single_post_service(_id) # returns post entity
        return jsonify(Post.to_dict()) # entity to dict

    def get_single_post_comments_controller(self, _id):
        print ('Post controller')
        Post =  self.post_service.get_single_post_comments_service(_id) # returns post entity
        return jsonify(Post.to_dict()) # entity to dict