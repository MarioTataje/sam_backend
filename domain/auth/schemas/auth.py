from marshmallow import post_load, post_dump, validates_schema
from werkzeug.security import generate_password_hash
from extensions.exception_extension import BadRequestException
from extensions.database_extension import ma
from domain.accounts.models.user import User


class LoginSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "password")
        model = User

    @validates_schema()
    def validate_tag(self, data, **kwargs):
        errors = {}
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            errors['email'] = 'Email is required'
        if email == '':
            errors['email'] = 'Email must not be blank'
        if password is None:
            errors['password'] = 'Password is required'
        if password == '':
            errors['password'] = 'Password must not be blank'
        if errors:
            raise BadRequestException(errors)


class RegisterSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password", "dni")
        model = User

    @validates_schema()
    def validate_user(self, data, **kwargs):
        errors = {}
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        email = data.get('email', None)
        password = data.get('password', None)
        dni = data.get('dni', None)
        if first_name is None:
            errors['first_name'] = 'First Name is required'
        if first_name == '':
            errors['first_name'] = 'First Name must not be blank'
        if last_name is None:
            errors['last_name'] = 'Last Name is required'
        if last_name == '':
            errors['last_name'] = 'Last Name must not be blank'
        if email is None:
            errors['email'] = 'Email is required'
        if email == '':
            errors['email'] = 'Email must not be blank'
        if password is None:
            errors['password'] = 'Password is required'
        if password == '':
            errors['password'] = 'Password must not be blank'
        if dni is None:
            errors['dni'] = 'Dni is required'
        if dni == '':
            errors['dni'] = 'Dni must not be blank'
        if errors:
            raise BadRequestException(errors)

    @post_dump()
    def get_data(self, data, **kwargs):
        del data['password']
        return data

    @post_load
    def make_user(self, data, **kwargs):
        data['password'] = generate_password_hash(data['password'])
        return User(**data)
