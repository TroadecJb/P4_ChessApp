from tinydb import TinyDB, Query, where

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")


class Match:
    """Class for a match"""

    victory = 1
    loss = 0
    draw = 0.5

    def __init__(self, index):
        self.index = index
        # self.players_list = ""
        self.player_1 = ""
        self.player_2 = ""
        self.match_result = ""
        self.serialized = {
            "match_index": "",
            "player_1": "",
            "player_2": "",
            "match_result": "",
        }

    def __repr__(self):
        return f"{self.index}\njoueurs : {self.player_1}, {self.player_2}\n{self.match_result}"

    def serialize(self):
        self.serialized = {
            "match_index": self.index,
            "player_1": self.player_1.doc_id,
            "player_2": self.player_2.doc_id,
            "match_result": self.match_result,
        }
        return self.serialized

    def deserialize(self, data):  # chelou
        self.index = data["index"]
        self.players_list = data["players_list"]
        self.player_1 = data["player_1"]
        self.player_2 = data["player_2"]
        self.match_result = data["match_result"]

    def set_result(self):
        prompt = input(
            f"Indiquer le résultat pour le match {self.index} ? (y/n)\n"
        ).lower()
        if prompt == "y":
            result = input(
                f"Entrez le numéro du joueur gagnant, 1 : {self.player_1} | 2 : {self.player_2} | 3 : Match nul \n"
            )
            if result == "1":
                self.player_1.points += Match.victory
                self.player_2.points += Match.loss
                self.match_result = f"victoire de {self.player_1}"
            elif result == "2":
                self.player_1.points += Match.loss
                self.player_2.points += Match.victory
                self.match_result = f"victoire de {self.player_2}"
            elif result == "3":
                self.player_1.points += Match.draw
                self.player_2.points += Match.draw
                self.match_result = "match nul"
            else:
                print("Entrez 1, 2 ou 3.")
            self.serialize()
        else:
            pass
