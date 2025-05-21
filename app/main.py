from init_db import session, db_connected
from models.service.menu import Menu 

if db_connected:
    menu = Menu(session)
    menu.affichage()
else:
    print("❌ La base de données n'est pas connectée.")