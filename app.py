from flask import Flask
from extensions.config_extension import register_config
from extensions.database_extension import register_database
from extensions.security_extension import register_security
from extensions.routes_extension import register_routes
from extensions.exception_extension import register_exception_handler


def create_app():
    app = Flask(__name__)
    register_config(app)
    register_database(app)
    register_security(app)
    app.app_context().push()
    register_routes(app)
    register_exception_handler(app)
    return app
