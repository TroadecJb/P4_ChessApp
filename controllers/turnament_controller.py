from models import tournoi, tour, joueur
from controllers import pairing_system


class Tournoi_controller:
    def __init__(self):
        self.pair_system = pairing_system.Swiss_system()

    def create_turnament():
        prompt = input("Souhaitez vous créer un nouveau tournoi ? (y/n)\n").lower()
        if prompt == "y":
            new_turnament = tournoi.Tournoi()
            new_turnament.set_name()
            new_turnament.set_date()
            new_turnament.set_place()
            new_turnament.set_number_rounds()
            new_turnament.set_time_mode()
            new_turnament.add_players_to_turnament()
            new_turnament.serialize()
            return new_turnament
        else:
            pass

    def add_players_to_turnament(tournoi):
        potential_player = []
        selected_player = []
        adding_player = True

        prompt = input(
            "Voulez-vous ajouter des joueurs dans ce tournoi ? (y/n)\n"
        ).lower()

        if prompt == "y":
            for idx, player in enumerate(JOUEUR_TABLE):
                name = (player["last_name"], player["first_name"])
                print(f"{idx + 1} : {name}")
                potential_player.append(name)

            while adding_player:
                selection = input(
                    "Entrez l'index des joueurs participant au tournoi (pour arrêter n'entrez aucun index et validez):\n"
                )
                # if the user press enter without typing anything the input return will be empty : the length of it will 0.
                if len(selection) > 0:
                    selected_player.append(potential_player[int(selection) - 1])
                else:
                    adding_player = False

            for player in selected_player:
                player = joueur.Joueur()
                player = player.deserialize()
                tournoi.players_list.append(player)
        else:
            pass

    def generate_first_round(tournoi_):
        """
        Generate first round for the turnament, with paired players according to pairing system.
        """
        index = len(tournoi_.matchs_list)
        first_round = tour.Tour(index)
        tournoi_.rounds_list.append(first_round)

        for player in tournoi.players_list:
            player.reset_points()

        round_one = tournoi_.rounds_list[O]
        pairs_list = self.pair_sys.generate_inital_pairs(tournoi_.players_list)

        for idx, pair in enumerate(pairs_list):
            round_one.matchs_list.append(
                Match(idx, pair)
            )  # tester si il ne faut pas créer une variable pour l'ajouter à une liste

    def generate_round(tournoi_):
        """
        Generate next round, if in range of turnament's number of round.
        Pairs according to pairing system (no pair redundancy).
        """
        index = len(tournoi_.matchs_list)
        if index <= tournoi_.number_of_rounds:
            next_round = tour.Tour(index)

            pairs_list = self.pair_sys.generate_pairs(tournoi_.players_list)

            for idx, pair in enumerate(pairs_list):
                next_round.matchs_list.append(
                    Match(idx, pair)
                )  # tester si il ne faut pas créer une variable pour l'ajouter à une liste

            tournoi_.rounds_list.append(next_round)
        else:
            pass
