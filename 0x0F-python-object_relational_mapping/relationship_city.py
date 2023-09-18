#!/usr/bin/python3
"""
Defines a State model.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    Represents a state for a MySQL database.

    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'cities'
    id = Column(
        Integer, primary_key=True, unique=True,
        nullable=False, autoincrement=True
        )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
