from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManager

from jobplus.config import configs
from jobplus.models import db, User

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
        
    login_manager.login_view = 'front.login'

def register_blueprints(app):
    from .handlers import front, job, company, admin, user, tests
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(company)
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(tests)

def register_error_hanlers(app):

    @app.errorhandler(404)
    def not_ound(error):
        return render_template('error/404.html'),404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('error/500.html'),500

def create_app(config):

    app = Flask(__name__)

    if isinstance(config,dict):
        app.config.update(config)
    else:
        app.config.from_object(configs.get(config,None))

    db.init_app(app)
    Migrate(app,db)
    register_blueprints(app)
    register_extensions(app)
    register_error_hanlers(app)
    return app

