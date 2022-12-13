from tinydb import TinyDB, Query, where
from models import tournoi, joueur

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Controller_db:
    def add_player_to_table_players(JOUEUR_TABLE):
        adding_entry = True
        while adding_entry:
            last_name = input("Indiquez le nom du joueur :\n").lower()
            first_name = input("Indiquez le prénom du joueur :\n").lower()
            name = f"{first_name} {last_name}"
            birth_date = input(
                f"Indiquez la date de naissance (dd/mm/yyyy) :\n"
            ).lower()
            gender = input(f"Indiquez le genre de {name} : \n").lower()
            rank = input(f"Indiquez le classement de {name} :\n").lower()
            JOUEUR_TABLE.insert(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "birth_date": birth_date,
                    "gender": gender,
                    "rank": rank,
                }
            )
            prompt = input(
                "Ajouter un autre joueur à la base de donnée ? (y/n)\n"
            ).lower()
            if prompt == "y":
                adding_entry = True
            else:
                adding_entry = False

    def search_player():
        last_name = input("Entrez le nom de famille du joueur :\n").lower()
        first_name = input("Entrez le prénom du joueur :\n").lower()
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

    def search_turnament():
        turnament_name = input("Entrez le nom du tournoi :\n").lower()
        turnament_date = input("Entrez la date du tournoi :\n").lower()
        turnament_place = input("Entrez le lieu du tournoi :\n").lower()

        turnament_data = TOURNOI_TABLE.search(
            (where("name") == turnament_name)
            & (where("date") == turnament_date)
            & (where("place") == turnament_place)
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

    def save(x, table):
        x.serialize()
        table.insert(x.serialized)

    def update(object, table):
        pass
