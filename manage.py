#!/usr/bin/env python

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from lyrics import create_app
from lyrics.models import db

app = create_app('lyrics.config.DevConfig')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, db=db)


if __name__ == "__main__":
    manager.run()
