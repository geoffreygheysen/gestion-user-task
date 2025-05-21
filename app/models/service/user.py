# dependances
from sqlalchemy import text
from models.db.user import User as UserModel
from .db_tools import DbTools # outil de base pour session + commit

class User(DbTools):
    
    def __init__(self, session):
        super().__init__(session)
        
    # <-----    METHODES    ----->
    
    # Créer un utilisateur
    def create(self, username, email, password):
        user = UserModel(username=username, email=email, password=password)
        self.session.add(user)
        self.commit()
        return user
    
    # Afficher tous les utilisateurs
    def display(self):
        return self.session.query(UserModel).all()
    
    # Rechercher un utilisateur par email
    def search_by_email(self, email):
        return self.session.query(UserModel).filter(
            UserModel.email.ilike(f"%{email}%")
        ).all()
    
    # Rechercher un utilisateur par id 
    def search_by_id(self, id_):
        return self.session.query(UserModel).filter_by(id=id_).first()
        
    # Modifier un utilisateur
    def update(self, id_, new_username=None, new_email=None, new_password=None):
        u = self.search_by_id(id_)
        if u:
            if new_username is not None:
                u.username = new_username
            if new_email is not None:
                u.email = new_email
            if new_password is not None:
                u.password = new_password
            self.commit()
        return u
    
    # Supprimer un utilisateur
    def delete(self, id_):
        u = self.search_by_id(id_)
        if u:
            self.session.delete(u)
            self.commit()
            return True
        return False
    
    # Afficher les détails
    def show_details(self, user):
        print(f"Username : {user.username}")
        print(f"Email : {user.email}")
        print("Tasks :")
        for t in user.tasks:
            print(f" - {t.description}")