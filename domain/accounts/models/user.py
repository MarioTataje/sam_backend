from extensions.database_extension import db, BaseModel


class User(db.Model, BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(200), nullable=True)
    dni = db.Column(db.String(200), nullable=False)

    def __init__(self, first_name, last_name,  email, password, dni, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.dni = dni
        self.phone = phone

