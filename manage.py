import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from dash import app
from dash.models import db

app.config.from_object(os.environ['APP_SETTINGS'])

MIGRATE = Migrate(app, db)
MANAGER = Manager(app)
MANAGER.add_command('db', MigrateCommand)

if __name__ == '__main__':
    MANAGER.run()
