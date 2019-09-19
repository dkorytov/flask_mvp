from flask import Flask

flask_instance = Flask(__name__)

from application_folder import routes
