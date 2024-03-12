from flask import Flask
from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler
import os

from project import create_app

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()