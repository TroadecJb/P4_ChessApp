from tinydb import TinyDB, Query, where
from models import tournoi, joueur, tour, match, exceptions
from views.user_input import User_choice
import operator

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")

user_input = User_choice()


class Controller_db:
    """exchange between DB and program"""

    def get_doc_id(self, table):
        table_data = table.all()
        ids = [item.doc_id for item in table_data]
        return ids

    def get_all_turnaments(self):
        """Return a list of every turnament in the table"""
        turnaments_data = TOURNOI_TABLE.all()
        liste = [turnament for turnament in turnaments_data]

        return liste

    def add_players_to_DB(self, players_data):
        """Add to players_data to the table JOUEUR_TABLE"""
        JOUEUR_TABLE.insert_multiple(players_data)

    def get_players_from_DB(self):
        """Retrieve player from database, based on user selection, returns the list of class Joueur"""
        players_list = []
        index_players = []
        adding_player = True

        for player in JOUEUR_TABLE:
            print(f"{player.doc_id} -", player["last_name"], player["first_name"])

        players_ids = self.get_doc_id(JOUEUR_TABLE)

        while adding_player:
            prompt = "Entrez l'index des joueurs que vous souhaitez modifier :\n(pour arrêter n'entrez aucun index et validez]\n"
            print(prompt)
            choice = user_input.int_range_input(players_ids)
            if len(choice) > 0:
                index_players.append(choice)
            else:
                adding_player = False

        for index in index_players:
            player_data = JOUEUR_TABLE.get(doc_id=index)
            player = joueur.Joueur()
            player.deserialize(player_data)
            players_list.append(player)

        return players_list

    def retrieve_turnament(self):
        """Returns serialized turnament from table."""
        turnament_list = []
        selected_turnament = ""
        turnament_data = TOURNOI_TABLE.all()

        if turnament_data:
            for turnament in TOURNOI_TABLE:
                print(
                    f"{turnament.doc_id} -",
                    turnament["name"],
                    turnament["date"],
                    turnament["place"],
                )
            turnament_ids = self.get_doc_id(TOURNOI_TABLE)
            prompt = "Sélectionnez le numéro du tournoi voulu :"
            print(prompt, "\n")

            choice = user_input.int_range_input(turnament_ids)
            selected_turnament = TOURNOI_TABLE.get(doc_id=choice)

            return selected_turnament
        else:
            message = "Aucun tournoi dans la base de donnée."
            print(message)

    def deserialize_turnament(self, turnament_serialized):
        """Deserializes turnament, deserializes every players, rounds and matchs."""
        turnament = tournoi.Tournoi()

        turnament.name = turnament_serialized["name"]
        turnament.place = turnament_serialized["place"]
        turnament.date = turnament_serialized["date"]
        turnament.number_of_rounds = int(turnament_serialized["number_of_rounds"])

        turnament.players_list = []
        for p in turnament_serialized["players_list"]:
            player = joueur.Joueur()

            player_data = JOUEUR_TABLE.get(doc_id=p)

            player.deserialize(player_data)
            turnament.players_list.append(player)

        turnament.matchs_list = []
        turnament.rounds_list = []
        for t in turnament_serialized["rounds_list"]:
            tour_class = tour.Tour(t["round_index"])

            tour_class.matchs_list = []
            for m in t["matchs_list"]:
                match_class = match.Match(m["match_index"])
                match_class.match_result = m["match_result"]
                player_1 = [
                    player
                    for player in turnament.players_list
                    if player.doc_id == m["player_1"]
                ]
                player_2 = [
                    player
                    for player in turnament.players_list
                    if player.doc_id == m["player_2"]
                ]
                match_class.player_1 = player_1[0]
                match_class.player_2 = player_2[0]
                tour_class.matchs_list.append(match_class)

                turnament.matchs_list.append(
                    [match_class.player_1.doc_id, match_class.player_2.doc_id]
                )

            tour_class.start_time = t["start_time"]
            tour_class.end_time = t["end_time"]
            turnament.rounds_list.append(tour_class)

        turnament.time_mode = turnament_serialized["time_mode"]
        turnament.description = turnament_serialized["description"]
        turnament.doc_id = turnament_serialized.doc_id

        return turnament

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
        """Update JOUEUR_TABLE with serialized player's data, based on doc_id."""
        x.serialize()
        JOUEUR_TABLE.update(x.serialized, doc_ids=[x.doc_id])

    def update_turnament(self, Tournoi):
        """Update TOURNOI_TABLE with serialized turnament's data, based on doc_id."""
        Tournoi.serialize()
        TOURNOI_TABLE.update(Tournoi.serialized, doc_ids=[Tournoi.doc_id])
