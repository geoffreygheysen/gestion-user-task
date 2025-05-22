from passlib.context import CryptContext

# On crée un contexte de hachage sécurisé avec bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash un mot de passe simple en hash sécurisé"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compare un mot de passe fourni avec un hash stocké"""
    return pwd_context.verify(plain_password, hashed_password)
