from api.auth.routes import auth_blueprint


def register_routes(app):
    print('app')
    app.register_blueprint(auth_blueprint)
    #app.register_blueprint(profiles_blueprint)
    #app.register_blueprint(medical_risks_blueprint)
    #app.register_blueprint(medical_monitoring_blueprint)
