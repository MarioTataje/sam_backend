from flask_jwt_extended import JWTManager

jwt = JWTManager()


def register_security(app):

    jwt.init_app(app)
