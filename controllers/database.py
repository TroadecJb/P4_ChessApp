from tinydb import TinyDB, Query, where
from models import tournoi, joueur

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
            (where("first_name") == first_name) & (where("last_name") == last_name)
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

    def save(self, x, table):
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
