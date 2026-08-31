from enum import Enum

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Location(Enum):
    CAIRO = "Cairo"
    ALEXANDRIA = "Alexandria"
