from tinydb import TinyDB, Query, where

db = TinyDB("db.json")


class Match:
    """Class for a match"""

    def __init__(self, index, players_list):
        self.index = index
        self.players_list = players_list
