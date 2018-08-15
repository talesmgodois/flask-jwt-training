from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import environments


app = Flask(__name__)

api = Api(app)



app.config.from_object(environments.app_config['development'])

db = SQLAlchemy(app)

import views, models, resources

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run()