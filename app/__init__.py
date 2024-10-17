from flask import Flask                                               
from config import Config
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from flask_login import LoginManager

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

login = LoginManager(flask_app)

from app import routes, models