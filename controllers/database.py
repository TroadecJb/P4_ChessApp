from tinydb import TinyDB, Query, where
from models import tournoi, joueur, tour, match
import operator

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Controller_db:
    """exchange between DB and program"""

    def get_all_turnaments(self):
        turnaments_data = TOURNOI_TABLE.all()
        liste = [turnament for turnament in turnaments_data]

        return liste

    def add_players_to_DB(self, players_data):
        """Add to players_data to the table JOUEUR_TABLE"""
        JOUEUR_TABLE.insert_multiple(players_data)

    # def show_players(self):
    #     print("liste des joueurs:\n")
    #     for player in JOUEUR_TABLE:
    #         print(f"\t", player["last_name"], player["first_name"])

    # def search_player(self, info):
    #     index_data = 0
    #     player_data = JOUEUR_TABLE.search(
    #         (where("first_name") == {info[0]}) & (where("last_name") == {info[1]})
    #     )
    #     if len(player_data) < 1:
    #         for idx, i in enumerate(player_data):
    #             print(idx + 1, i)
    #         index_data = input("Entrez l'index du joueur souahité :\n")
    #         confirmation = input(
    #             f"Confirmez la sélection du joueur suivant (y/n) :\n{player_data[index_data-1]}\n"
    #         )
    #     else:
    #         pass
    #     return player_data[index_data]

    def get_players_from_DB(self):
        """Retrieve player from database, based on user selection, returns the list of class Joueur"""
        players_list = []
        index_players = []
        adding_player = True

        for player in JOUEUR_TABLE:
            print(f"{player.doc_id} - {player.last_name} {player.first_name}")

        while adding_player:
            choice = input(
                "Entrez l'index des joueurs que vous souhaitez modifier :\n(pour arrêter n'entrez aucun index et validez]\n"
            )
            if len(choice) > 0:
                index_players.append(choice)
            else:
                adding_player = False

        Player = Query()
        for index in index_players:
            player_data = JOUEUR_TABLE.search(Player.doc_id == index)
            player = joueur.Joueur()
            player.deserialize(player_data)
            players_list.append(player)

        return players_list

    def search_turnament(
        self, info
    ):  # problème avec la confirmation de sélection, dans tous les cas un tournoi est retourné
        turnament_data = TOURNOI_TABLE.search(
            (where("name") == info[0])
            & (where("date") == info[1])
            & (where("place") == info[2])
        )
        if len(turnament_data) < 1:
            for idx, i in enumerate(turnament_data):
                print(idx + 1, i)
            index_data = input("Entrez l'index du tournoi souahité :\n")
            confirmation = input(
                f"Confirmez la sélection du tournpo suivant (y/n) :\n{turnament_data[index_data-1]}\n"
            )
        else:
            pass
        return turnament_data[index_data]

    def retrieve_turnament(self):
        turnament_list = []
        selected_turnament = ""

        for turnament in TOURNOI_TABLE:
            turnament_list.append(turnament)

        for idx, turnament in enumerate(turnament_list):
            print(
                f"{idx + 1} -", turnament["name"], turnament["date"], turnament["place"]
            )

        choice = input("Sélectionnez le numéro du tournoi voulu :\n")
        selected_turnament = turnament_list[int(choice) - 1]

        return selected_turnament

    def deserialize_turnament(self, turnament_serialized):
        turnament = tournoi.Tournoi()

        turnament.name = turnament_serialized["name"]
        turnament.place = turnament_serialized["place"]
        turnament.date = turnament_serialized["date"]
        turnament.number_of_rounds = int(turnament_serialized["number_of_rounds"])

        turnament.players_list = []
        for p in turnament_serialized["players_list"]:
            player_class = joueur.Joueur()

            player = Query()
            player_data = JOUEUR_TABLE.search(p.doc_id == player.doc_id)

            player_class.deserialize(player_data)
            turnament.players_list.append(player_class)

        turnament.rounds_list = turnament_serialized["rounds_list"]
        turnament.matchs_list = turnament_serialized["matchs_list"]
        turnament.time_mode = turnament_serialized["time_mode"]
        turnament.description = turnament_serialized["description"]

        return turnament

    def deserialize_round(self, Tournoi):
        rounds_list = []
        for t in Tournoi.rounds_list:
            tour_class = tour.Tour(t["round_index"])
            tour_class.matchs_list = t["matchs_list"]
            tour_class.start_time = t["start_time"]
            tour_class.end_time = t["end_time"]
            rounds_list.append(tour_class)

        Tournoi.rounds_list = rounds_list

    def deserialize_match(self, Tournoi):
        matchs_list = []
        for t in Tournoi.rounds_list:
            for m in t.matchs_list:
                match_class = match.Match(m["match_index"])
                match_class.match_result = m["match_result"]
                match_class.player_1 = [
                    player
                    for player in Tournoi.players_list
                    if player.doc_id == m["player_1"]
                ]
                match_class.player_2 = [
                    player
                    for player in Tournoi.players_list
                    if player.doc_id == m["player_2"]
                ]
                matchs_list.append(match_class)
            t.matchs_list = matchs_list

    def save_turnament(self, Tournoi):
        """From class object to serialize attr, stored in table."""
        Tournoi.serialize()
        TOURNOI_TABLE.insert(Tournoi.serialized)

    def save_player(self, player):
        """From class object to serialize attr, stored in table."""
        if type(player) == list:
            for i in player:
                i.serialize()
                JOUEUR_TABLE.insert(i.serialized)
        else:
            player.serialize()
            JOUEUR_TABLE.insert(player.serialized)

    def update_player(self, x):
        if type(x) == list:
            for i in x:
                i.serialize()
                JOUEUR_TABLE.update(i.serialized)
        else:
            x.serialize()
            JOUEUR_TABLE.update(x.serialized)

    def update_turnament(self, Tournoi):
        Tournoi.serialize()
        TOURNOI_TABLE.update(Tournoi.serialized)

    # def deserialize(self, data):
    #     self.name = db["name"]
    #     self.place = db["place"]
    #     self.date = db["date"]
    #     self.number_of_rounds = db["number_of_round"]
    #     self.rounds_list = db["rounds_list"]
    #     self.players_list = db["players"]
    #     self.time_mode = db["time_mode"]
    #     self.description = db["description"]
