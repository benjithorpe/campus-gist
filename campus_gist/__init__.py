import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Initialize the extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
# redirect un-authenticated users to login page
login_manager.login_view = "login_page"


from campus_gist import routes, models, errors
