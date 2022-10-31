from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


# function to create web application
def create_app():
    app = Flask(
        __name__,
        static_url_path='',
        static_folder='templates/static',
        template_folder='templates',
        instance_relative_config=False
        )
    path_to_current_file = os.path.abspath(__file__)
    print(path_to_current_file)
    app.debug = True
    app.secret_key = "myComputerShopSecret"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path_to_current_file + '/../myComputerShopDatabase.db'
    db.init_app(app)
    from .views import view
    app.register_blueprint(view)
    from .rest import rest
    app.register_blueprint(rest)
    return app
