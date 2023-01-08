from views.user_input import UserChoice

CHESS_TIME_MODE = ["", "bullet", "blitz", "coup rapide"]

user_input = UserChoice()


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
        # self.serialized = {}

    def __str__(self):
        return f"\n{self.name} a lieu à {self.place}, le {self.date}.\nLes participants sont {self.players_list}.\nC'est en tournoi en {self.number_of_rounds} tour(s) avec un contrôle de temps {self.time_mode}."

    def __repr__(self):
        return f"\nTournoi(nom={self.name}, lieu={self.place}, date={self.date}, nombre_de_tour={self.number_of_rounds}, mode={self.time_mode}, participants={self.players_list}."

    def set_name(self):
        prompt = "Entrez le nom du tournoi :\n"
        print(prompt)
        turnament_name = user_input.user_input()

        self.name = turnament_name

    def set_date(self):
        prompt = "Entrez la date du tournoi (dd/mm/yyyy):\n"
        print(prompt)
        turnament_date = user_input.user_input()
        self.date = turnament_date

    def set_place(self):
        prompt = "Entrez le lieu du tournoi :\n"
        print(prompt)
        turnament_place = user_input.user_input()
        self.place = turnament_place

    def set_time_mode(self):
        choice = int(
            input(
                f"Sélectionner le mode de Contrôle du temps :\n 1 - Bullet\n 2 - Blitz\n 3 - Coup Rapide\n"
            )
        )
        choice = user_input.int_range_input([1, 2, 3])
        self.time_mode = CHESS_TIME_MODE[choice]

    def set_number_rounds(self):
        prompt = (
            "Le nombre de tour par défaut est de 4, voulez-vous le modifier ? (y/n)\n"
        )
        print(prompt)
        choice = user_input.user_input()
        if choice == "y":
            prompt = "Indiquez le nombre de tour pour ce tournoi :\n"
            print(prompt)
            choice = user_input.int_input()
            self.number_of_rounds = choice
        else:
            self.number_of_rounds = 4

    def add_players(self, selected_player):
        self.players_list.append(selected_player)

    def redo_players(self, selec_player):
        self.players_list = []
        self.players_list

    def add_description(self):
        prompt = "Voulez-vous ajotuer une description ? (y/n)\n"
        print(prompt)
        choice = user_input.user_input()
        if choice == "y":
            prompt = "Entrez votre description :\n"
            print(prompt)
            description = user_input.user_input()
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

        # self.serialized = {
        #     "name": self.name,
        #     "place": self.place,
        #     "date": self.date,
        #     "number_of_rounds": self.number_of_rounds,
        #     "rounds_list": rounds_list,
        #     "players_list": players_list,
        #     "matchs_list": self.matchs_list,
        #     "time_mode": self.time_mode,
        #     "description": self.description,
        #     "doc_id": self.doc_id,
        # }

        # return self.serialized
        serialized = vars(self)
        serialized["rounds_list"] = rounds_list
        serialized["players_list"] = players_list
        return serialized

    def update_info(self):
        self.set_name()
        self.set_date()
        self.set_place()
        self.set_time_mode()
        self.set_number_rounds()
