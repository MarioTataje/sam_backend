from api.auth.adapters.docs.auth import auth_namespace
from flask_restx import fields


login_request = auth_namespace .model('LoginRequest', {
   'email': fields.String(required=True),
   'password': fields.String(required=True)
})

register_request = auth_namespace .model('RegisterRequest', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
    'phone': fields.String(required=True),
    'dni': fields.String(required=True)
})

forgot_password_request = auth_namespace .model('ForgotPasswordRequest', {
    'email': fields.String(required=True)
})

reset_password_request = auth_namespace .model('ResetPasswordRequest', {
    'token': fields.String(required=True),
    'password': fields.String(required=True)
})
