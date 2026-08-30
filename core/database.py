from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class Location(enum.Enum):
    Cairo = "Cairo"
    Alexandria = "Alexandria"
