CHESS_TIME_MODE = ["bullet", "blitz", "coup rapide"]


class Tournoi:
    """Class for a turnament"""

    def __init__(self):
        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_rounds = ""
        self.rounds_list = []
        self.players_list = []
        self.matchs_list = []
        self.time_mode = ""
        self.description = ""
        self.doc_id = ""
        self.serialized = {}

    def __str__(self):
        return f"\n{self.name} a lieu à {self.place}, le {self.date}.\nLes participants sont {self.players_list}.\nC'est en tournoi en {self.number_of_rounds} tour(s) avec un contrôle de temps {self.time_mode}."

    def __repr__(self):
        return f"\nTournoi(nom={self.name}, lieu={self.place}, date={self.date}, nombre_de_tour={self.number_of_rounds}, mode={self.time_mode}, participants={self.players_list}."

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
            choice = input("Indiquez le nombre de tour pour ce tournoi :\n")
            try:
                int(choice)
                self.number_of_rounds = int(choice)
            except ValueError:
                print("Entrez un nombre pour le nombre de tour.\n")
                self.set_number_rounds()
        else:
            self.number_of_rounds = 4
            print("\t", self.number_of_rounds, type(self.number_of_rounds))

    def add_players(self, selected_player):
        self.players_list = selected_player

    def add_description(self):
        prompt = input("Voulez-vous ajotuer une description ? (y/n)\n").lower()
        if prompt == "y":
            description = input("Entrez votre description :\n")
            self.description = description
        else:
            pass

    def serialize(self):
        players_list = []
        for player in self.players_list:
            players_list.append(player.doc_id)

        rounds_list = []
        for r in self.rounds_list:
            x = r.serialize()
            rounds_list.append(x)

        # matchs_list = []
        # for m in self.matchs_list:
        #     print(type(m), m)
        #     x = m.serialize()
        #     matchs_list.append(x)

        self.serialized = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_of_rounds": self.number_of_rounds,
            "rounds_list": rounds_list,
            "players_list": players_list,
            "matchs_list": self.matchs_list,
            "time_mode": self.time_mode,
            "description": self.description,
            "doc_id": self.doc_id,
        }

        return self.serialized
