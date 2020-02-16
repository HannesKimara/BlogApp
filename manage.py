from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Blog, Comment

app = create_app('development')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('serve', Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Blog = Blog, Comment = Comment)

if __name__ == '__main__':
    manager.run()
