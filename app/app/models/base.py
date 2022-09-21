from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import as_declarative, declarative_base
from sqlalchemy.orm import declared_attr, scoped_session, sessionmaker

from app.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
Base.query = db_session.query_property()