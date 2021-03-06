import os
from flask import Flask, request
from controllers.UserController import UserController
from service.UserService import UserService
from dataAccessLayer.UserQueries import UserQueries

userQueries = UserQueries()
userService = UserService(userQueries)
userCtrl = UserController(userService)

from controllers.PostController import PostController
from service.PostService import PostService
from dataAccessLayer.PostsQueries import PostsQueries

from dataAccessLayer.CommentsQueries import CommentsQueries

postQueries = PostsQueries()
commentsQueries = CommentsQueries()
postService = PostService(postQueries,commentsQueries)
postCtrl = PostController(postService)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.ProductionConfig')
    #app.config.from_envvar('APP_CONFIG')  
    #app.config.from_pyfile('config.py')
    return app

app = create_app()


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/user/<int:_id>', methods=['GET'])
def get_user(_id):
    return userCtrl.get_user_controller(_id)

@app.route('/users', methods=['GET'])
def get_all_user():
    return userCtrl.get_all_user_controller()

@app.route('/post/<int:_id>', methods=['GET'])
def get_post(_id):
    return postCtrl.get_single_post_controller(_id)
    
@app.route('/post-comments/<int:_id>', methods=['GET'])
def get_post_with_comments(_id):
    return postCtrl.get_single_post_comments_controller(_id)
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
