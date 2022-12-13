from tinydb import TinyDB, Query, where
from models import tournoi, joueur

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Controller_db:
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

    def save(self, item, table):
        if type(item) == list:
            for x in item:
                table.insert(x)
        else:
            table.insert(item)

    def update(self, object, table):
        pass
