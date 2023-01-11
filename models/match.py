from views.user_input import UserChoice

user_input = UserChoice()


class Match:
    """Class for a match"""

    victory = 1
    loss = 0
    draw = 0.5

    def __init__(self, index):
        self.index = index
        self.player_1 = ""
        self.player_2 = ""
        self.match_result = ""

    def __repr__(self):
        return f"{self.index}\njoueurs : {self.player_1}, {self.player_2}\n{self.match_result}"

    def serialize(self):
        serialized = {
            "index": self.index,
            "player_1": self.player_1.doc_id,
            "player_2": self.player_2.doc_id,
            "match_result": self.match_result,
        }

        return serialized

    def deserialize(self, data):  # chelou
        self.index = data["index"]
        self.players_list = data["players_list"]
        self.player_1 = data["player_1"]
        self.player_2 = data["player_2"]
        self.match_result = data["match_result"]

    def set_result(self):
        prompt = f"Indiquer le résultat pour le match {self.index} ? (y/n)\n"
        print(prompt)
        choice = user_input.str_range_input(["y", "n"])

        if choice == "y":
            prompt = f"Entrez le numéro du joueur gagnant, 1 : {self.player_1} | 2 : {self.player_2} | 3 : Match nul \n"
            print(prompt)
            result = user_input.str_range_input(["1", "2", "3"])
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
            self.serialize()
        else:
            pass
