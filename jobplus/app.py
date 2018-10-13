from .handlers import front, course, admin


def register_blueprints(app):
	app.register_blueprint(front)
	app.register_blueprint(course)
	app.register_blueprint(admin)

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(configs.get(config))
	db.init_app(app)
	register_blueprint(app)
	return app