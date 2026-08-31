from datetime import UTC, datetime
from enum import Enum as PyEnum

from geoalchemy2 import Geography
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from core.database import Base


class InterestStatus(PyEnum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"


class ProposalStatus(PyEnum):
    pending = "Pending"
    confirmed = "Confirmed"


class Interest(Base):
    __tablename__ = "interests"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    interested_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(InterestStatus), default=InterestStatus.pending)
    created_at = Column(DateTime, default=datetime.now(UTC))

    __table_args__ = (
        UniqueConstraint(
            "book_id", "interested_user_id", name="unique_user_book_interest"
        ),
    )

    book = relationship("Book", back_populates="interests")
    interested_user = relationship(
        "User",
        back_populates="interested_books",
        foreign_keys=[interested_user_id],
    )
    proposals = relationship("Proposal", back_populates="interest")


class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True)
    interest_id = Column(Integer, ForeignKey("interests.id"))
    proposed_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    proposed_date = Column(DateTime, default=datetime.now(UTC))
    proposed_location = Column(
        Geography(geometry_type="POINT", srid=4326), nullable=False
    )
    message = Column(String, nullable=True)
    status = Column(Enum(ProposalStatus), default=ProposalStatus.pending)
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=datetime.now(UTC), onupdate=datetime.now(UTC))

    interest = relationship("Interest", back_populates="proposals")
    proposed_by = relationship(
        "User",
        back_populates="proposals_made",
        foreign_keys=[proposed_by_user_id],
    )
