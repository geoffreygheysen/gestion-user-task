# gestion-user-task

Projet de mise en place d’une application console basée sur SQLAlchemy, en manipulant plusieurs entités liées à la gestion d'utilisateurs et de tâches.

Documentation étapes par étapes du projet:

---

## 📁 Mise en place du projet

### Setup du dossier de l'application et ses fichiers (app) 📂

        - app/
            - models/
                - db/
                    - base.py
                    - task.py
                    - user.py
                - service/
                    - db_tools.py
                    - task.py
                    - user.py
                    - menu.py
            - init_db.py
            - main.py
        - .gitignore
        - README.md
        - requirements.txt

### Utilité des différents dossiers et fichiers de l'application.

    📂 app/
        Dossier principal de l'application. Tout le code source se trouve ici.

        🔹 models/
            Ce dossier contient la logique métier et la structure des données. Il est divisé en deux sous-dossiers :

            🔸 db/
                Contient les modèles de base de données définis avec un ORM (ici SQLAlchemy).

                base.py : définit la base commune de tous tes modèles (Base = declarative_base()). C’est la fondation de l'ORM.

                task.py : définit le modèle Task (structure d’une tâche : id, description).

                user.py : définit le modèle User (structure d’un utilisateur : username, email, password, is_active).

            🔸 service/
                Contient la logique métier associée aux modèles — fonctions de manipulation ou de gestion des objets User, Task, etc.

                db_tools.py : outils pour interagir avec la base (ex : création de session, gestion des connexions...).

                task.py : logique de gestion des tâches.

                user.py : logique pour gérer les utilisateurs.

                menu.py : gérer l’affichage des menus.

        📄 init_db.py
            Script qui permet de créer ou initialiser ta base de données.

        📄 main.py
            Point d’entrée principal de l'application.
            C’est ce fichier que tu exécutes pour lancer l'app !

    📄 .gitignore
        Fichier qui indique à Git quels fichiers ou dossiers ignorer (ex : .venv/, __pycache__/, config.py).

    📄 README.md
        Contient la documentation du projet : description, instructions d’installation, comment lancer l’app, etc.

    📄 requirements.txt
        Liste des dépendances Python de ton projet. Utilisé pour installer tous les paquets nécessaires avec

---

## ⚙️ Création et activation de l’environnement virtuel

```bash
# Création de l’environnement virtuel
py -3 -m venv .venv

# Activation de l’environnement (Windows)
.\.venv\Scripts\activate
```

---

## ⚙️ Installation du fichier requirements.txt

```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuration de la base PostgreSQL

Avec pgAdmin 4: Créer une database (ex: db_gestion-user-task)

Ensuie dans un fichier `config.py`, renseignez vos informations de connexion PostgreSQL :

```python
# Paramètres de connexion
scheme         = "postgresql+psycopg2"
username       = "votre_utilisateur"
password       = "votre_mot_de_passe"
hostname       = "localhost"
port           = "5432"
database_name  = "nom_de_votre_base"

# Construction de l'URL de connexion
URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"
```

### Position du fichier config.py

```python

        - app/
            - models/
                - db/
                    - base.py
                    - task.py
                    - user.py
                - service/
                    - db_tools.py
                    - task.py
                    - user.py
                    - menu.py
            - `config.py`
            - init_db.py
            - main.py
        - .gitignore
        - README.md
        - requirements.txt

```

## 🚀 Lancement

Une fois votre base de données PostgreSQL prête et vos entités définies, lancez simplement :

```bash
python app/main.py
```

---
