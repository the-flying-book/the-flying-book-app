from datetime import UTC, datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class Location(PyEnum):
    CAIRO = "Cairo"
    ALEXANDRIA = "Alexandria"


class BookCondition(PyEnum):
    NEW = "New"
    GOOD = "Good"
    FAIR = "Fair"
    POOR = "Poor"


class BookStatus(PyEnum):
    available = "Available"
    pending = "Pending"
    sold = "Sold"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    condition = Column(Enum(BookCondition), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    location = Column(Enum(Location), nullable=False)
    status = Column(Enum(BookStatus), default=BookStatus.available)
    price = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now(UTC))

    owner = relationship("User", back_populates="books")
    interests = relationship("Interest", back_populates="book")
