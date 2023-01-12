from views.user_input import UserChoice
from controllers.turnament import TournoiController

CHESS_TIME_MODE = ["", "bullet", "blitz", "coup rapide"]

user_input = UserChoice()
tournoi_controller = TournoiController()


class Tournoi:
    """Class for a turnament"""

    def __init__(self):
        self.doc_id = ""
        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_rounds = ""
        self.rounds_list = []
        self.current_round = ""
        self.players_list = []
        self.matchs_list = []
        self.time_mode = ""
        self.description = ""

    def __str__(self):
        message = (
            f"\n{self.name} a lieu à {self.place}, le {self.date}."
            f"\nLes participants sont {self.players_list}."
            f"\nC'est en tournoi en {self.number_of_rounds} tour(s) avec un contrôle de temps {self.time_mode}."
        )
        return message

    def __repr__(self):
        message = (
            f"\nTournoi(nom={self.name}, lieu={self.place}, date={self.date}"
            f"\nnombre_de_tour={self.number_of_rounds}, mode={self.time_mode}"
            f"\nparticipants={self.players_list}."
        )
        return message

    def set_name(self):
        """Set Tounoi's name."""

        prompt = "\nEntrez le nom du tournoi :"
        print(prompt)
        turnament_name = user_input.user_input()

        self.name = turnament_name

    def set_date(self):
        """Set Tournoi's date."""

        prompt = "\nEntrez la date du tournoi (dd/mm/yyyy):"
        print(prompt)
        turnament_date = user_input.user_input()
        self.date = turnament_date

    def set_place(self):
        """Set Tournoi's place."""

        prompt = "\nEntrez le lieu du tournoi :"
        print(prompt)
        turnament_place = user_input.user_input()
        self.place = turnament_place

    def set_time_control(self):
        """Set Tournoi's time control."""

        prompt = (
            "\nSélectionner le mode de Contrôle du temps :\n"
            "\t1 - Bullet\n"
            "\t2 - Blitz\n"
            "\t3 - Coup Rapide\n"
        )

        print(prompt)
        choice = user_input.int_range_input([1, 2, 3])
        self.time_mode = CHESS_TIME_MODE[choice]

    def set_number_rounds(self):
        """Set Tournoi's number of rounds(Tour)."""

        prompt = (
            "\nLe nombre de tour par défaut est de 4, voulez-vous le modifier ? (y/n)"
        )
        print(prompt)
        choice = user_input.user_input()
        if choice == "y":
            prompt = "\nIndiquez le nombre de tour pour ce tournoi :"
            print(prompt)
            choice = user_input.int_input()
            self.number_of_rounds = choice
        else:
            self.number_of_rounds = 4

    def add_players(self, selected_player):
        """Add a list to Tournoi's players list."""

        self.players_list.append(selected_player)

    def add_description(self):
        """Set Tournoi's description."""

        prompt = "\nVoulez-vous ajouter une description ? (y/n)"
        print(prompt)
        choice = user_input.user_input()
        if choice == "y":
            prompt = "\nEntrez votre description :"
            print(prompt)
            description = user_input.user_input()
            self.description = description
        else:
            pass

    def serialize(self):
        """Serialize Tounroi information."""

        players_list = []
        if self.players_list:
            for player in self.players_list:
                players_list.append(player.doc_id)

        rounds_list = []
        if self.rounds_list:
            for r in self.rounds_list:
                x = r.serialize()
                rounds_list.append(x)

        serialized = {
            "doc_id": self.doc_id,
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_of_rounds": self.number_of_rounds,
            "rounds_list": rounds_list,
            "current_round": self.current_round,
            "players_list": players_list,
            "matchs_list": self.matchs_list,
            "time_mode": self.time_mode,
            "description": self.description,
        }

        return serialized

    def update_info(self):
        """Allow user to update/change every information of Tournoi"""

        self.__repr__()
        self.set_name()
        self.set_date()
        self.set_place()
        self.set_time_control()
        self.set_number_rounds()
        tournoi_controller.redo_players_list(self)
        self.add_description()
