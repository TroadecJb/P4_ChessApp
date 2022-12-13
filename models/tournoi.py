CHESS_TIME_MODE = ["bullet", "blitz", "coup rapide"]


class Tournoi:
    """Class for a turnament"""

    def __init__(self):
        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_rounds = 4
        self.rounds_list = []
        self.players_list = []
        self.matchs_list = []
        self.time_mode = ""
        self.description = ""
        self.index_in_table = ""
        self.serialized = ""

    def __str__(self):
        print(
            f"{self.name} a lieu à {self.place}, le {self.date}.\nLes participants sont {self.players_list}.\nC'est en tournoi en {self.number_of_rounds} tour(s) avec un contrôle de temps {self.time_mode}."
        )

    def __repr__(self):
        print(
            f"Tournoi(nom={self.name}, lieu={self.place}, date={self.date}, nombre_de_tour={self.number_of_rounds}, mode={self.time_mode}, participants={self.players_list}."
        )

    def set_name(self):
        turnament_name = input("Entrez le nom du tournoi :\n")
        self.name = turnament_name

    def set_date(self):
        turnament_date = input("Entrez la date du tournoi (dd/mm/yyyy):\n")
        self.date = str(turnament_date)

    def set_place(self):
        turnament_place = input("Entrez le lieu du tournoi :\n")
        self.place = turnament_place

    def set_time_mode(self):
        choice = int(
            input(
                f"Sélectionner le mode de Contrôle du temps :\n 1 - Bullet\n 2 - Blitz\n 3 - Coup Rapide\n"
            )
        )
        if choice < 4:
            self.time_mode = CHESS_TIME_MODE[choice - 1]
        else:
            self.time_mode = "pas de choix effectué"

    def set_number_rounds(self):
        prompt = input(
            "Le nombre de tour par défaut est de 4, voulez-vous le modifier ? (y/n)\n"
        ).lower()
        if prompt == "y":
            choice = int(input("Indiquez le nombre de tour pour ce tournoi :\n"))
            if choice is type(int):
                self.number_of_rounds = choice
            else:
                pass
        else:
            pass

    def add_description(self):
        prompt = input("Voulez-vous ajotuer une description ? (y/n)\n").lower()
        if prompt == "y":
            description = input("Entrez votre description :\n")
            self.description = description
        else:
            pass

    def serialize(self):
        self.serialized = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_of_round": self.number_of_rounds,
            "rounds_list": self.rounds_list,
            "players": self.players_list,
            "matchs_list": self.matchs_list,
            "time_mode": self.time_mode,
            "description": self.description,
        }

    def deserialize(self, db):
        self.name = db["name"]
        self.place = db["place"]
        self.date = db["date"]
        self.number_of_rounds = db["number_of_round"]
        self.rounds_list = db["rounds_list"]
        self.players_list = db["players"]
        self.matchs_list = db["matchs_list"]
        self.time_mode = db["time_mode"]
        self.description = db["description"]
