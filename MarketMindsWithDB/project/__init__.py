from flask import Flask
from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler
import os
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)
    initialize_extensions(app)  
    register_blueprints(app)
    register_error_pages(app)  


    return app

def register_blueprints(app):
    # Import the blueprints
    from project.stocks import stocks_blueprint
    from project.users import users_blueprint

    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    app.register_blueprint(stocks_blueprint)
    app.register_blueprint(users_blueprint, url_prefix='/users')





from flask import Flask, render_template


def register_error_pages(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('405.html'), 405

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_login import LoginManager



convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

# Create the instances of the Flask extensions in the global scope,
# but without any arguments passed in. These instances are not
# attached to the Flask application at this point.
database = SQLAlchemy(metadata=metadata)


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    database.init_app(app)
    db_migration.init_app(app, database)
    csrf_protection.init_app(app)  
    login.init_app(app)

    from project.models import User

    @login.user_loader
    def load_user(user_id):
        query = database.select(User).where(User.id == int(user_id))
        return database.session.execute(query).scalar_one()

...




database = SQLAlchemy(metadata=metadata)
db_migration = Migrate()
csrf_protection = CSRFProtect() 
login = LoginManager()            
login.login_view = "users.login" 

