from sqlalchemy import *
from sqlalchemy.orm import (
    scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///database.sqlit3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    time = Column(DateTime, default=func.now())
    description = Column(String)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship(
        Section,
        backref=backref('tasks',
                        uselist=True,
                        cascade='delete,all'))
