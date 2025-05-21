# dependances
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

# Création de ma class Task qui va hériter de Base
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    
    # Relation vers l'utilisateur (chaque tâche appartient à un utilisateur)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="tasks")