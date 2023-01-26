import sqlalchemy as sa
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    password_hash = sa.Column(sa.Text)


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    date = sa.Column(sa.Date)
    kind = sa.Column(sa.String)
    amount = sa.Column(sa.Numeric(10, 2))
    title = sa.Column(sa.String, nullable=False)
    minTitle = sa.Column(sa.String, nullable=False)
    backImage = sa.Column(sa.String, nullable=True)
    logoImage = sa.Column(sa.String, nullable=True)
    tags = sa.Column(ARRAY(Text), nullable=True)
