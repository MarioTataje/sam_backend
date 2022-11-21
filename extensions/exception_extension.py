from werkzeug.exceptions import HTTPException
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
from jwt import DecodeError, ExpiredSignatureError


class BadRequestException(HTTPException):
    code = 400

    def __init__(self, data):
        super().__init__(data)


class NotFoundException(HTTPException):
    code = 404

    def __init__(self, data, attribute, value):
        message = f'The {data} was not found with the given {attribute}: {value}'
        super().__init__(message)


class EmailException(HTTPException):
    code = 422

    def __init__(self):
        message = f'The email that you have chosen is already taken'
        super().__init__(message)


class InternalServerException(HTTPException):
    code = 500

    def __init__(self):
        message = 'Internal server error has occurred'
        super().__init__(message)


def handle_exception(error: HTTPException):
    response = {
        'error': error.__class__.__name__,
        'message': error.description
    }
    return response, error.code


def handle_no_token(error):
    response = {
        'error': error.__class__.__name__,
        'message': 'No token found'
    }
    return response, error.code


def handle_invalid_header(error):
    response = {
        'error': error.__class__.__name__,
        'message': 'Token is invalid'
    }
    return response, error.code


def handle_expires_token(error):
    response = {
        'error': error.__class__.__name__,
        'message': 'The token has expired'
    }
    return response, error.code


def register_exception_handler(app):
    app.register_error_handler(NoAuthorizationError, handle_no_token)
    app.register_error_handler(InvalidHeaderError, handle_invalid_header)
    app.register_error_handler(ExpiredSignatureError, handle_expires_token)
    app.register_error_handler(DecodeError, handle_invalid_header)
    app.register_error_handler(BadRequestException, handle_exception)
    app.register_error_handler(NotFoundException, handle_exception)
    app.register_error_handler(EmailException, handle_exception)
    app.register_error_handler(InternalServerException, handle_exception)
