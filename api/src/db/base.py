from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.inspection import inspect


class CustomBase:
    #  Generate __tablename__ automagically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Serializer:
    def serialize(self):
        return {
            c: getattr(self, c)
            for c in inspect(self).attrs.keys()
        }

    @staticmethod
    def serialize_list(list_):
        return [l.serialize() for l in list_]


Base = declarative_base(cls=CustomBase)
