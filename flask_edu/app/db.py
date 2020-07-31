from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
import click

db = SQLAlchemy()

from .model import User

def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db)

@click.command('init-db')
@with_appcontext
def init_db():
    print('try init db')
    db.create_all()
    print('db init succeed')


