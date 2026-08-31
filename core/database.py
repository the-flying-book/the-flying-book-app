from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from core.config import settings

Base = declarative_base()

engine = create_engine(url=settings.POSTGRES_URL, echo=True, pool_pre_ping=True)

sessionFactory = sessionmaker(bind=engine, autoflush=False)


def get_db() -> Generator[Session, None, None]:
    db = sessionFactory()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    from modules.users import models  # noqa
    from modules.books import models  # noqa
    from modules.interests import models  # noqa

    Base.metadata.create_all(bind=engine)
    print("Database tables created.")


def drop_db() -> None:
    Base.metadata.drop_all(bind=engine)
    print("Database tables dropped.")
