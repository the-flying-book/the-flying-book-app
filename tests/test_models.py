from sqlalchemy import inspect

from modules.books.models import Book
from modules.interests.models import Interest, Proposal
from modules.users.models import User


def test_models_and_relationships_are_wired_correctly():
    assert User.__tablename__ == "users"
    assert Book.__tablename__ == "books"
    assert Interest.__tablename__ == "interests"
    assert Proposal.__tablename__ == "proposals"

    user_relationships = {rel.key for rel in inspect(User).relationships}
    book_relationships = {rel.key for rel in inspect(Book).relationships}
    interest_relationships = {rel.key for rel in inspect(Interest).relationships}
    proposal_relationships = {rel.key for rel in inspect(Proposal).relationships}

    assert {"books"}.issubset(user_relationships)
    assert {"interested_books", "proposals_made"}.issubset(user_relationships)
    assert {"owner", "interests"}.issubset(book_relationships)
    assert {"book", "interested_user", "proposals"}.issubset(interest_relationships)
    assert {"interest", "proposed_by"}.issubset(proposal_relationships)
