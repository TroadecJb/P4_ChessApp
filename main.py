from tinydb import TinyDB, Query, where
from models import joueur, tournoi, tour, match
from controllers.database import Controller_db
from controllers.turnament import Tournoi_controller
from controllers.pairing_system import Swiss_system
from views.database import DB_viewer
from datetime import datetime

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")

db_controller = Controller_db()
turnament_control = Tournoi_controller()


choice = input(
    "Que souhaitez vous faire ?\n"
    "1- Créer un tournoi\n"
    "2- Ajouter des joueurs à la base de donnes\n"
    "3- Lancer un tournoi \n"
)
if choice == "1":
    madchess = turnament_control.create_turnament()
    db_controller.save(madchess, TOURNOI_TABLE)
elif choice == "2":
    new_players = DB_viewer.new_player_info()
    db_controller.save(new_players, JOUEUR_TABLE)
elif choice == "3":
    turnament_index = db_controller.retrieve_turnament()
    turnament = tournoi.Tournoi()
    turnament.deserialize(turnament_index)
    if len(turnament.players_list) == 0:
        turnament.players_list = turnament_control.select_players_to_add()
        turnament.serialize()
        db_controller.update(turnament, TOURNOI_TABLE)
    turnament_control.generate_first_round(turnament)
