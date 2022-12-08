from tinydb import TinyDB, Query, where

db = TinyDB("db.json")


class Round:
    """Class for a round"""

    def __init__(self, index, matchs_list):
        self.index = index
        self.matchs_list = matchs_list
