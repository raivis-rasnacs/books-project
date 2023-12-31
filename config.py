"""Flask konfigurācija"""

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    MAINTENANCE_MODE = True if environ.get('MAINTENACE_MODE') == 'true' else False
    FLASK_ENV = environ.get("FLASK_ENV")

class DevConfig(Config):
    pass

class ProConfig(Config):
    pass