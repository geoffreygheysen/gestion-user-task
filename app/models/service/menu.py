import os
from models.service.user import User
from models.db.user import User as UserModel
from models.service.task import Task
from models.utils.security import verify_password
from models.utils.auth import login_user  # import de ta fonction centrale

class Menu:
    def __init__(self, session):
        self.session = session
        self.user = User(session)
        self.task = Task(session)
        self.current_user_id = None
        
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        input("\n⏎ Appuyez sur Entrée pour continuer...")

    def add_task_user(self, user_id):
        self.clear_console()
        description = input("Description de la tâche : ")
        user = self.user.search_by_id(user_id)
        if user:
            self.task.create_for_user(description, user)
            print("✅ Tâche ajoutée.")
        else:
            print("❌ Utilisateur introuvable.")
        self.pause()
        
    def get_current_user(self):
        if self.current_user_id is None:
            return None
        return self.session.query(UserModel).get(self.current_user_id)

    def affichage(self):
        while True:
            self.clear_console()
            current_user = self.get_current_user()

            if not current_user:
                # Menu sans utilisateur connecté
                print("\n🎮 Menu principal")
                print("1. Se connecter")
                print("2. Utilisateurs")
                print("0. Quitter")

                choix = input("Choix : ")
                if choix == "1":
                    user = login_user(self.session)
                    if user:
                        self.current_user_id = user.id
                        print(f"✅ Bienvenue {user.username} !")
                    else:
                        print("❌ Échec de la connexion.")
                    self.pause()

                elif choix == "2":
                    self.menu_user()
                elif choix == "0":
                    break
                else:
                    print("❌ Choix invalide.")
                    self.pause()
            else:
                # Menu utilisateur connecté
                print(f"\n🎮 Menu de {current_user.username}")
                print("1. Voir mes tâches")
                print("2. Ajouter une tâche")
                print("3. Se déconnecter")

                choix = input("Choix : ")
                if choix == "1":
                    self.menu_task(user_id=current_user.id)
                elif choix == "2":
                    self.add_task_user(current_user.id)
                elif choix == "3":
                    self.current_user_id = None
                else:
                    print("❌ Choix invalide.")
                    self.pause()

    def menu_user(self):
        self.clear_console()
        print("\n👨‍💼 UTILISATEURS")
        print("1. Ajouter")
        print("2. Lister")
        print("3. Chercher par email")
        print("4. Chercher par ID")
        print("5. Modifier")
        print("6. Supprimer")
        print("0. Retour")
        choix = input("Choix : ")

        if choix == "1":
            username = input("Nom d'utilisateur : ")
            email = input("Email : ")
            password = input("Mot de passe : ")
            self.user.create(username, email, password)
            print("✅ Utilisateur ajouté.")
            self.pause()

        elif choix == "2":
            for u in self.user.display():
                self.user.show_details(u)
            self.pause()

        elif choix == "3":
            email = input("Email (partiel) : ")
            results = self.user.search_by_email(email)
            for u in results:
                print(f"- {u.email}")
            self.pause()

        elif choix == "4":
            try:
                id_ = int(input("ID : "))
            except ValueError:
                print("❌ L’ID doit être un entier.")
                self.pause()
                return
            u = self.user.search_by_id(id_)
            if u:
                self.user.show_details(u)
            else:
                print("❌ Utilisateur introuvable.")
            self.pause()

        elif choix == "5":
            try:
                id_ = int(input("ID : "))
            except ValueError:
                print("❌ L’ID doit être un entier.")
                self.pause()
                return
            new_username = input("Nouveau nom : ")
            new_email = input("Nouvel email : ")
            new_password = input("Nouveau mot de passe : ")
            self.user.update(id_, new_username, new_email, new_password)
            self.pause()

        elif choix == "6":
            try:
                id_ = int(input("ID à supprimer : "))
            except ValueError:
                print("❌ L’ID doit être un entier.")
                self.pause()
                return
            self.user.delete(id_)
            self.pause()

    def menu_task(self, user_id=None):
        while True:
            self.clear_console()
            print("\n📝 TÂCHES")
            print("1. Ajouter une tâche à un utilisateur")
            print("2. Lister toutes les tâches")
            print("3. Lister les tâches d’un utilisateur")
            print("4. Modifier une tâche")
            print("5. Supprimer une tâche")
            print("0. Retour")
            choix = input("Choix : ")

            if choix == "1":
                try:
                    if user_id is None:
                        user_id_input = int(input("ID de l’utilisateur : "))
                    else:
                        user_id_input = user_id
                    self.add_task_user(user_id_input)
                except ValueError:
                    print("❌ L’ID doit être un entier.")
                    self.pause()

            elif choix == "2":
                for t in self.task.display():
                    print(f"[{t.id}] {t.description} (user_id={t.user_id})")
                self.pause()

            elif choix == "3":
                try:
                    if user_id is None:
                        user_id_input = int(input("ID de l’utilisateur : "))
                    else:
                        user_id_input = user_id
                    tasks = self.task.display(user_id=user_id_input)
                    if not tasks:
                        print("❌ Aucune tâche trouvée pour cet utilisateur.")
                    for t in tasks:
                        print(f"[{t.id}] {t.description}")
                except ValueError:
                    print("❌ L’ID doit être un entier.")
                self.pause()

            elif choix == "4":
                try:
                    task_id = int(input("ID de la tâche : "))
                    new_desc = input("Nouvelle description : ")
                    updated = self.task.update(task_id, new_desc)
                    if updated:
                        print("✅ Tâche mise à jour.")
                    else:
                        print("❌ Tâche introuvable.")
                except ValueError:
                    print("❌ L’ID doit être un entier.")
                self.pause()

            elif choix == "5":
                try:
                    task_id = int(input("ID de la tâche à supprimer : "))
                    deleted = self.task.delete(task_id)
                    if deleted:
                        print("✅ Tâche supprimée.")
                    else:
                        print("❌ Tâche introuvable.")
                except ValueError:
                    print("❌ L’ID doit être un entier.")
                self.pause()

            elif choix == "0":
                break

            else:
                print("❌ Choix invalide.")
                self.pause()
