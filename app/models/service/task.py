# dependances
from sqlalchemy import text
from models.db.user import User as UserModel
from models.db.task import Task as TaskModel
from .db_tools import DbTools # outil de base pour session + commit

class Task(DbTools):
    def __init__(self, session):
        super().__init__(session)
        
    # Créer une tâche pour un utilisateur donné
    def create_for_user(self, description, user):
        if user and not isinstance(user, UserModel):
            raise TypeError("L'utilisateur doit être une instance de UserModel ou None")
        
        task = TaskModel(description=description, user=user)
        self.session.add(task)
        self.commit()
        return task

    # Afficher toutes les tâches (ou par utilisateur)
    def display(self, user_id=None):
        query = self.session.query(TaskModel)
    
        if user_id is not None:
            query = query.filter(TaskModel.user_id == user_id)
        return query.all()
    
    # Chercher une tâches par id
    def search_by_id(self, id_):
        return self.session.query(TaskModel).filter_by(id=id_).first()
    
    # Modifier une tâche
    def update(self, id_, new_description):
        t = self.search_by_id(id_)
        
        if t:
            t.description = new_description
            self.commit()
        return t
    
    # Supprimer une tâche
    def delete(self, id_):
        t = self.search_by_id(id_)
        
        if t:
            self.session.delete(t)
            self.commit()
            return True
        return False
    
    # Afficher les détails
    def show_details(self, task):
        print(f"Tâche ID : {task.id}")
        print(f"Description : {task.description}")
        print(f"Assignée à : {task.user.username if task.user else 'Aucun utilisateur'}")