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

controller_db = Controller_db()
turnament_controller = Tournoi_controller()

jb = joueur.Joueur()
jb.doc_id = 1
jb.first_name = "jean-baptiste"
jb.last_name = "troadec"
jb.birth_date = "25/02/1993"
jb.gender = "homme"
jb.rank = 1

agathe = joueur.Joueur()
agathe.doc_id = 2
agathe.first_name = "agathe"
agathe.last_name = "legall"
agathe.birth_date = "27/10/1993"
agathe.gender = "femme"
agathe.rank = 2

pierre = joueur.Joueur()
pierre.doc_id = 3
pierre.first_name = "pîerre"
pierre.last_name = "Robes"
pierre.birth_date = "17/03/1750"
pierre.gender = "homme"
pierre.rank = 3

marie = joueur.Joueur()
marie.doc_id = 4
marie.first_name = "marie"
marie.last_name = "curie"
marie.birth_date = "31/11/1880"
marie.rank = 4

madchess = tournoi.Tournoi()
madchess.name = "madchess"
madchess.place = "guingamp"
madchess.date = "21/12/2022"
madchess.number_of_rounds = 3
madchess.time_mode = "bullet"
madchess.index_in_table = 1

madchess.players_list.extend([jb, agathe, pierre, marie])
turnament_controller.generate_first_round(madchess)

print(madchess)

for t in madchess.rounds_list:
    t.show_matchs()
    t.starting_time()
    print("\n")
    t.ending_time()

print(madchess)
for player in madchess.players_list:
    print(player.points)
