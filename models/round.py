from tinydb import TinyDB, Query, where
from datetime import datetime
from controllers import swiss_system

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Tour:
    """Class for a round"""

    def __init__(self, index):
        self.index = index
        self.matchs_list = []
        self.start_time = ""
        self.end_time = ""

    def set_match(self, list_pairs):
        """From tuple or list_pairs, generate a match"""

    def start_round(self):
        self.start_time = datetime.now()

    def end_round(self):
        self.end_time = datetime.now()
