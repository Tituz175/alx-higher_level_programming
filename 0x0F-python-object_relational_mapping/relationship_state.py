#!/usr/bin/python3
"""
Defines a State model.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, unique=True,
        nullable=False, autoincrement=True
        )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
