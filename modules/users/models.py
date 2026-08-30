from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base, Location


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    Location = Column(Enum(Location))

    books = relationship("Book", back_populates="owner")
