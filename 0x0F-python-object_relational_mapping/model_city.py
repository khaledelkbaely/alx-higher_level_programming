#!/usr/bin/python3
"""First state model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """State mapper to sql"""
    __tablename__ = "cities"
    id = Column(
        Integer, nullable=False, primary_key=True,
        unique=True, autoincrement=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
