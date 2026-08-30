import enum

from sqlalchemy import Column, DateTime, Enum, Integer, String

from core.database import Base


class Location(enum.Enum):
    Cairo = "Cairo"
    Alexandria = "Alexandria"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    Location = Column(Enum(Location))
