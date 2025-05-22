from models.db.user import User  # ton modèle
from models.utils.security import verify_password  # pour comparer les mots de passe

def login_user(session):
    email = input("Email : ")
    password = input("Mot de passe : ")

    user = session.query(User).filter_by(email=email).first()

    if not user:
        print("❌ Utilisateur introuvable.")
        return None

    if not user.is_active:
        print("⚠️ Compte inactif. Contactez un admin.")
        return None

    if not verify_password(password, user.password):
        print("❌ Mot de passe incorrect.")
        return None
    
    return user