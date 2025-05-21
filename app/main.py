from init_db import session, db_connected

if db_connected:
    print("✅ La DB est connectée ✅")
else:
    print("❌ La DB n'est pas connectée ❌")