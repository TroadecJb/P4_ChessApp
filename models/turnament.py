from tinydb import TinyDB, Query, where

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")
CHESS_TIME_MODE = ["bullet", "blitz", "coup rapide"]


def create_turnament():
    prompt = input("Souhaitez vous créer un nouveau tournoi ? (y/n)").lower()
    if prompt == "y":
        new_turnament = Tournoi()
        new_turnament.set_name()
        new_turnament.set_date()
        new_turnament.set_place()
        new_turnament.set_number_rounds()
        new_turnament.set_time_mode()
        new_turnament.add_players_to_turnament()
        new_turnament.serialize()
        new_turnament.save()
        print(f"{new_turnament.name} a été enregistré dans la base de données.")
        return new_turnament
    else:
        pass


class Tournoi:
    """Class for a turnament"""

    def __init__(self):
        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_rounds = 4
        self.rounds = []
        self.players_list = []
        self.time_mode = ""
        self.description = ""
        self.index_in_table = ""
        self.serialized = ""

    def __str__(self):
        print(
            f"{self.name} a lieu à {self.place}, le {self.date}.\nLes participants sont {self.players_list}.\nC'est en tournoi en {self.number_of_rounds} tour(s) avec un contrôle de temps {self.time_mode}."
        )

    def __repr__(self):
        print(
            f"Tournoi(nom={self.name}, lieu={self.place}, date={self.date}, nombre_de_tour={self.number_of_rounds}, mode={self.time_mode}, participants={self.players_list}."
        )

    def set_name(self):
        turnament_name = input("Entrez le nom du tournoi :\n")
        self.name = turnament_name

    def set_date(self):
        turnament_date = input("Entrez la date du tournoi :\n")
        self.date = str(turnament_date)

    def set_place(self):
        turnament_place = input("Entrez le lieu du tournoi :\n")
        self.place = turnament_place

    def set_time_mode(self):
        choice = int(
            input(
                f"Sélectionner le mode de Contrôle du temps :\n 1 - Bullet\n 2 - Blitz\n 3 - Coup Rapide\n"
            )
        )
        if choice < 4:
            self.time_mode = CHESS_TIME_MODE[choice - 1]
        else:
            self.time_mode = "pas de choix effectué"

    def set_number_rounds(self):
        prompt = input(
            "Le nombre de tour par défaut est de 4, voulez-vous le modifier ? (y/n)\n"
        ).lower()
        if prompt == "y":
            choice = int(input("Indiquez le nombre de tour pour ce tournoi :\n"))
            if choice is type(int):
                self.number_of_rounds = choice
            else:
                pass
        else:
            pass

    def add_description(self):
        prompt = input("Voulez-vous ajotuer une description ? (y/n)\n").lower()
        if prompt == "y":
            description = input("Entrez votre description :\n")
            self.description = description
        else:
            pass

    def add_players_to_turnament(self):
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
                if len(selection) > 0:
                    selected_player.append(potential_player[int(selection) - 1])
                else:
                    adding_player = False

            # Convert player into Class Joueur
            for player in selected_player:
                player = Joueur.deserialize()
                self.players_list.append(player)
        else:
            pass

    def serialize(self):
        self.serialized = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_of_round": self.number_of_rounds,
            "players": self.players_list,
            "time_mode": self.time_mode,
            "description": self.description,
        }

    def deserialize(self, db):
        self.name = db["name"]
        self.place = db["place"]
        self.date = db["date"]
        self.number_of_rounds = db["number_of_round"]
        self.players_list = db["players"]
        self.time_mode = db["time_mode"]
        self.description = db["description"]

    def save(self):  # vérifier pour une mis à jour d'un tournoi existant
        TOURNOI_TABLE.insert(self.serialized)
