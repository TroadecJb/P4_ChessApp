from tinydb import TinyDB, Query, where
from models import joueur, tournoi, tour, match
from controllers import database_controller, turnament_controller, swiss_system
from datetime import datetime

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")
