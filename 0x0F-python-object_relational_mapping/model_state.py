#!/usr/bin/python3
"""First state model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """State mapper to sql"""
    __tablename__ = "states"
    id = Column(
        Integer, nullable=False, primary_key=True,
        unique=True, autoincrement=True
    )
    name = Column(String(128), nullable=False)
