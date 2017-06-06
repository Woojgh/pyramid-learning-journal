from sqlalchemy import (
     Column,
     Integer,
     Unicode,
     Date,
)


from .meta import Base


class Entry(Base):
    '''.'''

    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    creation_date = Column(Date)
    entry = Column(Unicode)
