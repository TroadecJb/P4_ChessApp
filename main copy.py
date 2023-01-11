from tinydb import TinyDB, Query, where
from datetime import datetime
from models import joueur, tournoi, tour, match
from controllers.database import Controller_db
from controllers.turnament import Tournoi_controller
from controllers.pairing_system import Swiss_system
from views.database import DB_viewer


DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")

controller_db = Controller_db()
turnament_controller = Tournoi_controller()

##### joueurs #####
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
pierre.first_name = "pierre"
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

carl = joueur.Joueur()
carl.doc_id = 5
carl.first_name = "Carl"
carl.last_name = "Von linné"
carl.birth_date = "23/05/1707"
carl.rank = 5

Benazir = joueur.Joueur()
Benazir.doc_id = 6
Benazir.first_name = "Benazir"
Benazir.last_name = "Bhutto"
Benazir.birth_date = "21/06/1953"
Benazir.rank = 4

madchess = tournoi.Tournoi()
madchess.name = "madchess"
madchess.place = "guingamp"
madchess.date = "21/12/2022"
madchess.number_of_rounds = 3
madchess.time_mode = "bullet"
madchess.index_in_table = 1

##########

madchess.players_list.extend([jb, agathe, pierre, marie, carl, Benazir])

turnament_controller.run_turnament(madchess)
