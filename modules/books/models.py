from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base, Location


class BookCondition(Enum):
    NEW = "New"
    GOOD = "Good"
    FAIR = "Fair"
    POOR = "Poor"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    condition = Column(Enum(BookCondition), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    location = Column(Location)

    created_at = Column(DateTime, default=datetime.now(UTC))

    owner = relationship("User", back_populates="books")
