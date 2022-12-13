class Match:
    """Class for a match"""

    victory = 1
    loss = 0
    draw = 0, 5

    def __init__(self, index, players_list):
        self.index = index
        self.players_list = players_list
        self.player_1 = players_list[0].name
        self.player_2 = players_list[1].name
        self.player_1_result = ""
        self.player_2_result = ""

    def set_result(self):
        prompt = input(
            f"Indiquer le résultat pour le match {self.index} ? (y/n"
        ).lower()
        if prompt == "y":
            result = input(
                f"Entrez le numéro du joueur gagnant, 1 : {self.player_1} | 2 : {self.player_2} | 3 : Match nul \n"
            )
            if result == "1":
                self.player_1_result = victory
                players_list[0].points += victory
                self.player_2_result = loss
                players_list[0].points += loss
            elif result == "2":
                self.player_1_result = loss
                players_list[0].points += loss
                self.player_2_result = victory
                players_list[1].points += victory
            elif result == "3":
                self.player_1_result = draw
                players_list[0].points += draw
                self.player_2_result = draw
                players_list[1].points += draw
            else:
                print("Entrez 1, 2 ou 3.")
