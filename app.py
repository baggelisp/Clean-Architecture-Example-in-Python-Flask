import os
from flask import Flask, request
from controllers.UserController import UserController
from service.UserService import UserService
from dataAccessLayer.UserQueries import UserQueries

userQueries = UserQueries()
userService = UserService(userQueries)
userCtrl = UserController(userService)

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    return app

app = create_app()


@app.route('/')
def hello():
    print(os.environ['APP_SETTINGS'])
    return "Hello World!"


@app.route('/user/<int:_id>', methods=['GET'])
def get_user(_id):
    return userCtrl.get_user_controller(_id)



if __name__ == '__main__':
    app.run()
