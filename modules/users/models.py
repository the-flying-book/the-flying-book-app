from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    books = relationship("Book", back_populates="owner", foreign_keys="Book.owner_id")
    interested_books = relationship(
        "Interest",
        back_populates="interested_user",
        foreign_keys="Interest.interested_user_id",
    )
    proposals_made = relationship(
        "Proposal",
        back_populates="proposed_by",
        foreign_keys="Proposal.proposed_by_user_id",
    )
