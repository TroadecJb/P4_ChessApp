from tinydb import TinyDB, Query, where
from models import tournoi, tour, match, joueur
from controllers import pairing_system

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Tournoi_controller:
    def __init__(self):
        self.pair_system = pairing_system.Swiss_system()

    def create_turnament(self):
        prompt = input("Souhaitez vous créer un nouveau tournoi ? (y/n)\n").lower()
        if prompt == "y":
            new_turnament = tournoi.Tournoi()
            new_turnament.set_name()
            new_turnament.set_date()
            new_turnament.set_place()
            new_turnament.set_number_rounds()
            new_turnament.set_time_mode()
            # players_list = select_players_to_add()
            # new_turnament.add_players(players_list)
            return new_turnament
        else:
            pass

    def select_players_to_add(self):
        potential_player = []
        selected_player = []
        players_list = []
        adding_player = True

        prompt = input(
            "Voulez-vous ajouter des joueurs dans ce tournoi ? (y/n)\n"
        ).lower()

        if prompt == "y":
            # ajouter get doc_id
            for idx, player in enumerate(JOUEUR_TABLE):
                name = (player.doc_id, player["last_name"], player["first_name"])
                print(f"{idx + 1} : {name}")
                potential_player.append(player)

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
                new_player = joueur.Joueur()
                new_player.deserialize(player)
                players_list.append(new_player)

            return players_list
        else:
            pass

    def generate_first_round(self, tournoi_):
        """
        Generate first round for the turnament, with paired players according to pairing system.
        """
        index = len(tournoi_.rounds_list)
        first_round = tour.Tour(index)

        for player in tournoi_.players_list:
            player.reset_points()

        # round_one = tournoi_.rounds_list[O]
        pairs_list = self.pair_system.generate_inital_pairs(tournoi_.players_list)

        for idx, pair in enumerate(pairs_list):
            print(type(pair), pair)
            for i in pair:
                print(type(i), i)
            new_match = match.Match(f"tour {index}, match {idx}")
            new_match.player_1 = pair[0]
            new_match.player_2 = pair[1]

            first_round.matchs_list.append(new_match)

        tournoi_.rounds_list.append(first_round)

    def generate_round(self, tournoi_):
        """
        Generate next round, if in range of turnament's number of round.
        Pairs according to pairing system (no pair redundancy).
        """
        index = len(tournoi_.rounds_list)
        if index <= tournoi_.number_of_rounds:
            next_round = tour.Tour(index)

            pairs_list = self.pair_sys.generate_pairs(tournoi_.players_list)

            for idx, pair in enumerate(pairs_list):
                new_match = match.Match(f"tour {index}, match {idx}")
                new_match.players_list = pair
                next_round.matchs_list.append(new_match)

            tournoi_.rounds_list.append(next_round)
        else:
            pass

    def start_round(self, tournoi_):
        print(type(tournoi_.rounds_list[-1]), tournoi_.rounds_list[-1])
        current_round = tournoi_.rounds_list[-1]
        current_round.start_time()
        print(f"start_round: {current_round}")

    def end_round(self, tournoi_):
        current_round = tournoi_.round_list[-1]
        current_round.end_time()
        print(f"Ended_round : {current_round}")

    def run_turnament(self):
        pass
