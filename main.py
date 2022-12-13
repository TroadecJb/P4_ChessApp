from tinydb import TinyDB, Query, where
from models import joueur, tournoi, tour, match
from controllers import database_controller, turnament_controller, pairing_system

from datetime import datetime

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")

db_controller = database_controller.Controller_db()

choice = input(
    "Que souhaitez vous faire ?\n"
    "1- Créer un tournoi\n"
    "2- Ajouter des joueurs à la base de donnes\n"
)
if choice == "1":
    madchess = turnament_controller.create_turnament()
elif choice == "2":
    db_controller.add_player_to_table_players()
