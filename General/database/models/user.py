import datetime
from sqlalchemy import Column, String, BigInteger, DateTime

from ..db_base import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=True)
    balance = Column(BigInteger, nullable=False, default=0)
    latest_online = Column(DateTime, nullable=False, default=datetime.datetime.now())
    registration_date = Column(DateTime, nullable=False, default=datetime.datetime.now())
