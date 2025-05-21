# dependences
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from config import URL_DB

# import des modeles
from models.db.base import Base
from models.db import task, user

# initialisation des objets
engine = None
session = None
db_connected = False

try:
    # connexion à la DB
    engine = create_engine(URL_DB)
    
    # initialisation d'une session
    session = sessionmaker(bind=engine)
    session = session()
    
    # Base.metadata.drop_all(bind=engine)
    
    # Création des tables si elles n'existent pas 
    Base.metadata.create_all(bind=engine)
    
    db_connected = True
    print("<----------------------->")
    print("✅ Connexion DB + modèles créer ✅")
    print("<----------------------->")
except SQLAlchemyError as e:
    print("❌ Erreur de connexion à la DB : ❌")
    print(e)