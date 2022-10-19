# menu  package installed in your venv, globally, user space
from source import menu, access_func as af




DB_FILE = "./db/cafe_db.sql"


if __name__ == "__main__":
    menu.main_menu()
    af.initialize_db(DB_FILE)