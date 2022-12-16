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
    JOUEUR_TABLE.insert_multiple(new_players)

elif choice == "3":
    turnament_data = db_controller.retrieve_turnament()
    turnament = db_controller.deserialize_turnament(turnament_data)
    if len(turnament.players_list) == 0:
        turnament.players_list = turnament_control.select_players_to_add()
        # turnament.serialize()
        db_controller.update(turnament, TOURNOI_TABLE)
    turnament_control.generate_first_round(turnament)
    db_controller.update(turnament, TOURNOI_TABLE)
    turnament_control.start_round(turnament)
    db_controller.update(turnament, TOURNOI_TABLE)
    turnament_control.end_round(turnament)
    db_controller.update(turnament, TOURNOI_TABLE)

    # print(f"liste des tours: {turnament.rounds_list[0]}")
    # for player in turnament.players_list:
    #     print(type(player))
    #     print(player)
    # print(f"liste des joueurs: {turnament.players_list}")
    # turnament.rounds_list[O].show_matchs()

    #####
    # print(type(turnament))
    # print(turnament)
    # print(type(turnament.players_list))

    # for player in turnament.players_list:
    #     print(type(player))
    #     print(player)

    # turnament_control.generate_first_round(turnament)
    # db_controller.update(turnament, TOURNOI_TABLE)
