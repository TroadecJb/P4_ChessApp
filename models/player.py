from tinydb import TinyDB, Query, where

db = TinyDB("db.json")
db_players = db.table("players")


class Player:
    """Class for a player"""

    def __init__(self, first_name, last_name, date_birth, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{self.first_name} {self.last_name}"
        self.date_birth = date_birth
        self.gender = gender
        self.rank = rank

    def add_player_playersDb():
        adding_entry = True
        while adding_entry:
            last_name = input("Indiquez le nom du joueur :\n")
            first_name = input("Indiquez le prénom du joueur :\n")
            name = f"{first_name} {last_name}"
            birth_date = input(f"Indiquez la date de naissance de {name} :\n")
            gender = input(f"Indiquez le genre de {name} : \n")
            rank = input(f"Indiquez le classement de {name} :\n")
            db_players.table.insert(
                {
                    "first": first_name,
                    "last name": last_name,
                    "birth date": birth_date,
                    "gender": gender,
                    "rank": rank,
                }
            )
            prompt = input(
                "Ajouter un autre joueur à la base de donnée ? (y:n)\n"
            ).lower()
            if prompt != "y":
                adding_entry = False
            else:
                pass

    # def update_player():
