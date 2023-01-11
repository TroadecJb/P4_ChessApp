from tinydb import TinyDB
import operator
from views.user_input import UserChoice

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")

user_input = UserChoice()


class Rapport:
    def __init__(self):
        SORTING_LIST = ("alpha", "rank")

    def show_all_players(self):
        players_list = JOUEUR_TABLE.all()
        if players_list:
            print("\nListe des joueurs :\n")
            for player in JOUEUR_TABLE:
                readable = f'{player["last_name"].capitalize()} {player["first_name"].capitalize()}, classement: {player["rank"]}'
                print(readable, sep="\n")
        else:
            print("Aucun joueur dans la base donnée.")
            pass

    def show_turnament_players(self, Tournoi):
        if len(Tournoi.players_list) > 0:
            prompt = "Sélectionner le rangement  1- alphabétique | 2- classement\n"
            print(prompt)

            choice = user_input.str_range_input(["1", "2"])
            if choice == "1":
                liste = sorted(
                    Tournoi.players_list, key=operator.attrgetter("last_name")
                )
            elif choice == "2":
                liste = sorted(
                    Tournoi.players_list, key=operator.attrgetter("rank"), reverse=True
                )

            for player in liste:
                print(player)

        else:
            message = "Ce tournoi ne possède pas de joueurs."
            print(message)

    def show_all_turnaments(self):
        turnament_data = TOURNOI_TABLE.all()
        if turnament_data:
            prompt = "\nListe des tournois:"
            print(prompt)
            for turnament in turnament_data:
                readable = f'{turnament["name"]}, {turnament["date"]}, {turnament["place"]}.\ndescription: {turnament["description"]}\n'
                print(readable, sep="\n")
        else:
            message = "Aucun tournoi dans la base de donnée."
            print(message)
            pass

    def show_turnament_rounds(self, Tournoi):
        if len(Tournoi.rounds_list) > 0:
            rounds_list = [r for r in Tournoi.rounds_list]
            for r in rounds_list:
                print(r)
        else:
            message = "Ce tournoi ne semble pas encore avoir eu lieu et ne possède pas de tour."
            print(message)

    def show_turnament_matchs(self, Tournoi):
        if len(Tournoi.rounds_list) > 0:
            rounds_list = [r for r in Tournoi.rounds_list]
            for r in rounds_list:
                print(r.matchs_list)
        else:
            message = "Ce tournoi ne semble pas encore avoir eu lieu et ne possède pas de match"
            print(message)
