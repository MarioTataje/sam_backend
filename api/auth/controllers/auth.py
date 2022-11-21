import datetime
from flask import request, make_response
from flask_jwt_extended import create_access_token
from flask_restx import Resource
from werkzeug.security import check_password_hash
from api.auth.adapters.docs.auth import auth_namespace
from api.auth.adapters.requests.auth import login_request, register_request
from api.auth.adapters.responses.auth import login_response, login_unauthorized, register_response
from domain.accounts.models.user import User
from domain.auth.schemas.auth import LoginSchema, RegisterSchema


@auth_namespace.route('/login')
class LoginResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = LoginSchema()

    @auth_namespace.expect(login_request)
    @auth_namespace.response(code=200, description='Success', model=login_response)
    @auth_namespace.response(code=401, description='Unauthorized', model=login_unauthorized)
    def post(self):
        data = self.schema.load(request.get_json())
        email = data.get('email')
        password = data.get('password')
        user = User.get_one(**{'email': email})
        if not user:
            return make_response({'message': 'No user found with that email'}, 401)
        if check_password_hash(user.password, password):
            token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(hours=5))
            return make_response({'token': token}, 200)
        return make_response({'message': 'The credentials are wrong'}, 401)


@auth_namespace.route('/register')
class RegisterResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = RegisterSchema()

    @auth_namespace.expect(register_request)
    @auth_namespace.response(code=400, description='Bad Request')
    @auth_namespace.response(code=200, description='Success', model=register_response)
    def post(self):
        data = request.get_json()
        email = data.get('email')
        user = User.get_one(**{'email': email})
        if not user:
            user = self.schema.load(data)
            result = self.schema.dump(user.save())
            return result, 201
        else:
            return make_response({'message': 'User already exists. Please Log in'}, 202)
