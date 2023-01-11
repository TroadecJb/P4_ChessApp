from tinydb import TinyDB
from models import tournoi, tour, match, joueur
from controllers import pairing_system
from controllers.database import DbController
from views.user_input import UserChoice

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")

controller_db = DbController()
user_input = UserChoice()


class TournoiController:
    def __init__(self):
        self.pair_system = pairing_system.SwissSystem()

    def create_turnament(self):
        prompt = "\nSouhaitez vous créer un nouveau tournoi ? (y/n)"
        print(prompt)
        choice = user_input.str_range_input(["y", "n"])

        if choice == "y":
            new_turnament = tournoi.Tournoi()
            new_turnament.set_name()
            new_turnament.set_date()
            new_turnament.set_place()
            new_turnament.set_number_rounds()
            new_turnament.set_time_mode()
            self.add_players(new_turnament)
            new_turnament.current_round = 0
            new_id = controller_db.get_doc_id(TOURNOI_TABLE)
            new_turnament.doc_id = new_id[-1] + 1

            return new_turnament

        else:
            pass

    def show_players_list(self, Tournoi):
        print("\nListe des joueurs :")
        for player in Tournoi.players_list:
            print("\t", player)

    def check_players_list_odd_even(self, Tournoi):
        """If the players list is empty, ask to add players. Check if players list is odd or even and if odd ask to add or remove one player."""
        print("test check players", len(Tournoi.players_list))
        if len(Tournoi.players_list) > 0:
            if len(Tournoi.players_list) % 2 != 0:
                prompt = (
                    f"\nLes joueurs sont en nombre impair {len(Tournoi.players_list)}:\n"
                    "\t1 - ajouter un joueur"
                    "\t2 - supprimer un joueur"
                )
                print(prompt)
                choice = user_input.int_range_input([1, 2])
                if choice == 1:
                    self.add_one_player(Tournoi)
                    controller_db.update_turnament(Tournoi)
                    self.check_players_list_odd_even(Tournoi)
                else:
                    self.remove_one_player(Tournoi)
                    controller_db.update_turnament(Tournoi)
                    self.check_players_list_odd_even(Tournoi)

            else:
                return True
        else:
            self.add_players(Tournoi)
            self.check_players_list_odd_even(Tournoi)

    def add_players(self, Tournoi):
        """Takes user selection and retrieve players from the db and adds it to the turnament players list."""
        selected_player = []
        players_list = []
        adding_player = True

        if JOUEUR_TABLE.all():
            prompt = "\nVoulez-vous ajouter des joueurs dans ce tournoi ? (y/n)"
            print(prompt)
            choice = user_input.str_range_input(["y", "n"])
            players_ids = controller_db.get_doc_id(JOUEUR_TABLE)

            if choice == "y":
                for player in JOUEUR_TABLE.all():
                    print(player.doc_id, player["last_name"], player["first_name"])

                while adding_player:
                    prompt = "\nEntrez l'index des joueurs participant au tournoi (pour arrêter n'entrez aucun index et validez):"
                    print(prompt)
                    selection = user_input.int_range_input(players_ids)

                    if selection:
                        selected_player.append(JOUEUR_TABLE.get(doc_id=selection))
                        players_ids.remove(selection)

                    else:
                        adding_player = False

                for player in selected_player:
                    new_player = joueur.Joueur()
                    new_player.deserialize(player)
                    players_list.append(new_player)

                Tournoi.players_list = players_list

            else:
                pass

        else:
            print("Aucun joueur dans la base de données.")
            pass

    def add_one_player(self, Tournoi):
        """Takes user selection and retrieve player from the db and adds it to the turnament players list."""
        self.show_players_list(Tournoi)
        prompt = (
            "\nSélectionner l'index du joueur que vous souhaitez ajouter au tournoi:"
        )
        print(prompt)

        players_ids = [player.doc_id for player in JOUEUR_TABLE.all()]
        for player in JOUEUR_TABLE.all():
            print(f'{player.doc_id} : {player["last_name"]} {player["first_name"]}')
        choice = user_input.int_range_input(players_ids)

        selected_player = JOUEUR_TABLE.get(doc_id=choice)
        new_player = joueur.Joueur()
        new_player.deserialize(selected_player)
        Tournoi.players_list.append(new_player)

    def redo_players_list(self, Tournoi):
        """Empty the playes list and allows user to add players to it."""
        Tournoi.players_list = []
        print("\n Tous les joueurs ont été de la liste.")
        self.add_players()

    def remove_one_player(self, Tournoi):
        """Remove one player from the turnament players list."""
        self.show_players_list(Tournoi)

        prompt = (
            "\nSélectionner l'index du joueur que vous souhaitez retirer du tournoi:"
        )
        print(prompt)

        players_ids = [player.doc_id for player in Tournoi.players_list]
        for player in Tournoi.players_list:
            print(f"{player.doc_id} : {player}")

        choice = user_input.int_range_input(players_ids)
        player_to_remove = [
            player for player in Tournoi.players_list if player.doc_id == choice
        ]
        Tournoi.players_list.remove(player_to_remove[0])

    def remove_players(self, Tournoi):
        removing_player = True
        while removing_player:
            prompt = "\nEntrez l'index des joueurs que vous souhaitez retirer du tournoi (pour arrêtez n'entrez aucun index et validez):"
            print(prompt)
            players_ids = [player.doc_id for player in Tournoi.players_list]
            selection = user_input.int_range_input(players_ids)

            if selection:
                player_to_remove = [
                    player
                    for player in Tournoi.players_list
                    if player.doc_id == selection
                ]
                Tournoi.players_list.remove(player_to_remove[0])

            else:
                removing_player = False

    def modify_players_list(self, Tournoi, choice):
        if choice == 1:
            self.add_players(Tournoi)
        elif choice == 2:
            self.remove_players(Tournoi)

    def generate_first_round(self, Tournoi):
        """
        Generate first round for the turnament, with paired players according to pairing system.
        """
        index = 1
        first_round = tour.Tour(index)

        for player in Tournoi.players_list:
            player.reset_points()

        pairs_list = self.pair_system.generate_inital_pairs(Tournoi.players_list)

        for idx, pair in enumerate(pairs_list):
            new_match = match.Match(f"tour {index}, match {idx + 1}")
            new_match.player_1 = pair[0]
            new_match.player_2 = pair[1]

            first_round.matchs_list.append(new_match)
            Tournoi.matchs_list.append([getattr(joueur, "doc_id") for joueur in pair])

        Tournoi.rounds_list.append(first_round)

    def generate_round(self, Tournoi):
        """
        Generate next round, if in range of turnament's number of round.
        Pairs according to pairing system (no pair redundancy).
        """
        index = len(Tournoi.rounds_list) + 1
        next_round = tour.Tour(index)

        pairs_list = self.pair_system.generate_pairs(
            Tournoi.players_list, Tournoi.matchs_list
        )

        for idx, pair in enumerate(pairs_list):
            new_match = match.Match(f"tour {index}, match {idx + 1}")
            new_match.player_1 = pair[0]
            new_match.player_2 = pair[1]
            next_round.matchs_list.append(new_match)
            Tournoi.matchs_list.append([getattr(joueur, "doc_id") for joueur in pair])

        Tournoi.rounds_list.append(next_round)

    def start_round(self, Tournoi):
        current_round = Tournoi.rounds_list[Tournoi.current_round]
        current_round.starting_time()
        print(current_round)

    def end_round(self, Tournoi):
        current_round = Tournoi.rounds_list[Tournoi.current_round]
        current_round.ending_time()
        print(current_round)

    def run_turnament(self, Tournoi):
        players_list_check = self.check_players_list_odd_even(Tournoi)
        if players_list_check:
            while Tournoi.current_round < Tournoi.number_of_rounds:
                if Tournoi.current_round == 0:
                    self.generate_first_round(Tournoi)
                    self.start_round(Tournoi)
                    controller_db.update_turnament(Tournoi)
                    self.end_round(Tournoi)
                    Tournoi.current_round += 1
                    controller_db.update_turnament(Tournoi)
                else:
                    self.generate_round(Tournoi)
                    self.start_round(Tournoi)
                    controller_db.update_turnament(Tournoi)
                    self.end_round(Tournoi)
                    Tournoi.current_round += 1
                    controller_db.update_turnament(Tournoi)

            print(f"Tous les tours du tournoi {Tournoi.name} ont eu lieu.")
