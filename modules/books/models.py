from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base, Location


class bookCondition(Enum):
    new = "New"
    good = "Good"
    fair = "Fair"
    poor = "Poor"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    condition = Column(bookCondition)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    location = Column(Location)

    created_at = Column(DateTime, default=datetime.now(UTC))

    owner = relationship("User", back_populates="books")
