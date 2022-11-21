from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_seeder import FlaskSeeder


db = SQLAlchemy()
ma = Marshmallow()
seeder = FlaskSeeder()


class BaseModel:

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.merge(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def commit(self):
        if self:
            db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def get_one(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()


def register_database(app):
    db.init_app(app)
    Migrate(app, db)
    ma.init_app(app)
    # with app.app_context():
    #     db.create_all()
    seeder.init_app(app, db)
