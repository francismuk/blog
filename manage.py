from app import create_app, db
from flask_script import Manager, Server
# Connect to models
from app.models import User, Category
# Set up migrations
from flask_migrate import Migrate,MigrateCommand
import os

# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blog'


# Creating app instance
# app = create_app('test')
# app = create_app('development')
app = create_app('production')
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francis:1234@localhost/blogs'



# Create manager instance
manager = Manager(app)

# Create migrate instance
migrate = Migrate(app,db)

manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)


@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
   return dict(app=app, db=db, Category=Category)


if __name__ == '__main__':
    manager.run()
