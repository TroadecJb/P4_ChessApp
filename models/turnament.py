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