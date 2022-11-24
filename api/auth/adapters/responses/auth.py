from api.auth.adapters.docs.auth import auth_namespace
from flask_restx import fields


login_response = auth_namespace .model('LoginResponse', {
    'token': fields.String
})

login_unauthorized = auth_namespace .model('Unauthorized', {
   'message': fields.String('The credentials are wrong')
})

register_response = auth_namespace .model('RegisterResponse', {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'dni': fields.String
})

forgot_password_response = auth_namespace .model('ForgotPasswordResponse', {
    'message': fields.String('The email has been sent')
})

reset_password_response = auth_namespace .model('ResetPasswordResponse', {
    'message': fields.String('Your password has been changed')
})
