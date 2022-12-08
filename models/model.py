from tinydb import TinyDB, Query, where

db = TinyDB("db.json")

CHESS_TIME_MODE = ("bullet", "blitz", "coup rapide")

class Turnament:
    """Class for a turnament"""

    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = 4
        self.rounds = ""
        self.players = ""
        self.time_mode = ""
        self.description = ""

    turnament.create_turnament_db(turnament_name) # à mettre quelque part

    def turnament_db(self, name_db):
        name_db = db.table(self.name)
        name_db.insert({"nom": self.name, "place": self.place, "date": self.date})
   
    def create_turnament(self):
        prompt = input("Souhaitez vous créer un nouveau tournoi ? (y/n)").lower()
        if prompt == "y":
            self.set_name()
            self.set_date()
            self.set_place()
            self.set_number_rounds()
            self.set_time_mode()
            self.add_players_to_turnament()
            self.generate_rounds()
        else:
            pass
        
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
        choice = int(input(f"Sélectionner le mode de Contrôle du temps :\n 1 - Bullet\n 2 - Blitz\n 3 - Coup Rapide"))
        if choice is type(int) and choice < 4:
            self.time_mode = CHESS_TIME_MODE[choice]
        else:
            pass

    def set_number_rounds(self):
        prompt = input("Le nombre de tour par défaut est de 4, voulez-vous le modifier ? (y/n").lower()
        if prompt == 'y':
            choice = int(input("Indiquez le nombre de tour pour ce tournoi :\n"))
            if choice is type(int):
                self.number_of_rounds = choice
            else:
                pass
        else:
            pass
    
    def add_description(self):
        prompt = input("Voulez-vous ajotuer une description ? (y/n\n").lower()
        if prompt == 'y':
            description = input("Entrez votre description :\n")
            self.description = description
        else:
            pass

    def add_players_to_turnament(self):
        prompt = input("Voulez-vous ajouter des joueurs dans ce tournoi ? (y/n)\n").lower()
        if prompt == 'y':
            # ajouter fonction
        else:
            pass

    def generate_rounds(self):
        prompt = input("Voulez-vous générer générer la liste des tours ? (y/n)\n")
        if prompt == 'y':
            # générer la liste des tours
        else:
            pass


class Round:
    """Class for a round"""

    def __init__(self, index, matchs_list):
        self.index = index
        self.matchs_list = matchs_list


class Match:
    """Class for a match"""

    def __init__(self, index, players_list):
        self.index = index
        self.players_list = players_list


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
            players_db.insert(
                {
                    "first": first_name,
                    "last name": last_name,
                    "birth date": birth_date,
                    "gender": gender,
                    "rank": rank,
                }
            )
            prompt = input("Ajouter un autre joueur à la base de donnée ? (y:n)\n").lower()
            if prompt != 'y':
                adding_entry = False
            else:
                pass
    
    def update_player
