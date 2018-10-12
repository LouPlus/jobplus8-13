

def register_blueprints(app):
    from .handlers import front, job, company, admin, user, tests
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(company)
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(tests)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    return app
