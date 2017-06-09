from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(DateTime)

    def to_json(self):
        output = {}
        output['id'] = self.id
        output['title'] = self.title
        output['body'] = self.body
        output['creation_date'] = self.creation_date
        return output
