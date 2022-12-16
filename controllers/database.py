from tinydb import TinyDB, Query, where
from models import tournoi, joueur, tour, match
import operator

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Controller_db:
    def show_turnaments(self):
        print("liste des tournois:\n")
        for idx, turnament in enumerate(TOURNOI_TABLE):
            print(
                f"{idx}- ",
                turnament["name"],
                turnament["date"],
                turnament["place"],
                f"\n",
            )

    def show_players(self):
        print("liste des joueurs:\n")
        for player in JOUEUR_TABLE:
            print(f"\t", player["last_name"], player["first_name"])

    def search_player(self, info):
        index_data = 0
        player_data = JOUEUR_TABLE.search(
            (where("first_name") == {info[0]}) & (where("last_name") == {info[1]})
        )
        if len(player_data) < 1:
            for idx, i in enumerate(player_data):
                print(idx + 1, i)
            index_data = input("Entrez l'index du joueur souahité :\n")
            confirmation = input(
                f"Confirmez la sélection du joueur suivant (y/n) :\n{player_data[index_data-1]}\n"
            )
        else:
            pass
        return player_data[index_data]

    def search_turnament(self, info):
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
        turnament.number_of_rounds = int(turnament_serialized["number_of_round"])

        turnament.players_list = []
        for p in turnament_serialized["players_list"]:
            print(type(p), p)
            # player_data = self.search_player(p)
            player_class = joueur.Joueur()
            player_class.deserialize(p)
            turnament.players_list.append(player_class)

        turnament.rounds_list = []
        for t in turnament_serialized["rounds_list"]:
            tour_class = tour.Tour(t["round_index"])
            tour_class.deserialize(t)
            for m in tour_class.matchs_list:
                match_class = match.Match(
                    m["match_index"],
                )
                match_class.deserialize(m)
                match_class.players_list = [
                    player.doc_id == int(m.doc_id) for player in turnament.players_list
                ]

            turnament.rounds_list.append(tour_class)

        # turnament.matchs_list = db["matchs_list"]
        turnament.time_mode = turnament_serialized["time_mode"]
        turnament.description = turnament_serialized["description"]

        return turnament

    def save(self, x, table):
        """From class object to serialize var stored in table."""
        if type(x) == list:
            for i in x:
                i.serialize()
                table.insert(i.serialized)
        else:
            x.serialize()
            table.insert(x.serialized)

    def update(self, x, table):
        if type(x) == list:
            for i in x:
                i.serialize()
                table.update(i.serialized)
        else:
            x.serialize()
            table.update(x.serialized)

    # def deserialize(self, data):
    #     self.name = db["name"]
    #     self.place = db["place"]
    #     self.date = db["date"]
    #     self.number_of_rounds = db["number_of_round"]
    #     self.rounds_list = db["rounds_list"]
    #     self.players_list = db["players"]
    #     self.time_mode = db["time_mode"]
    #     self.description = db["description"]
