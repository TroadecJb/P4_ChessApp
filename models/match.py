class Match:
    """Class for a match"""

    victory = 1
    loss = 0
    draw = 0, 5

    def __init__(self, index):
        self.index = index
        self.player_1 = ""
        self.player_2 = ""
        self.match_result = ""

    def __repr__(self):
        return f"Match {self.index}| joueurs : {self.player_1}, {self.player_2}| {self.match_result}"

    def set_result(self):
        prompt = input(
            f"Indiquer le résultat pour le match {self.index} ? (y/n"
        ).lower()
        if prompt == "y":
            result = input(
                f"Entrez le numéro du joueur gagnant, 1 : {self.player_1} | 2 : {self.player_2} | 3 : Match nul \n"
            )
            if result == "1":
                self.player_1.points += victory
                self.player_2.points += loss
                self.match_result = f"victoire de {self.player_1}"
            elif result == "2":
                self.player_1.points += loss
                self.player_2.points += victory
                self.match_result = f"victoire de {self.player_2}"
            elif result == "3":
                self.player_1.points += draw
                self.player_2.points += draw
                self.match_result = "match nul"
            else:
                print("Entrez 1, 2 ou 3.")
