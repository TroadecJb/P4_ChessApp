from tinydb import TinyDB, Query, where
from pprint import pprint
import operator

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Rapport:
    def __init__(self):
        SORTING_LIST = ("alpha", "rank")

    def show_all_players(self):
        print("\nListe des joueurs :\n")
        for player in JOUEUR_TABLE:
            readable = f'{player["last_name"].capitalize()} {player["first_name"].capitalize()}, classement: {player["rank"]}'
            print(readable, sep="\n")

    def get_turnament_players(self, Tournoi):
        if len(Tournoi.players_list) > 0:
            sorting_choice = input(
                "Sélectionner le rangement  1- alphabétique | 2- classement\n"
            )
            if sorting_choice == "1":
                liste = sorted(
                    Tournoi.players_list, key=operator.attrgetter("last_name")
                )
            elif sorting_choice == "2":
                liste = sorted(Tournoi.players_list, key=operator.attrgetter("rank"))
            pprint(liste)
        else:
            message = "Ce tournoi ne possède pas de joueurs."
            pprint(message)

    def show_all_turnaments(self):
        turnament_data = TOURNOI_TABLE.all()
        if turnament_data:
            for turnament in turnament_data:
                readable = (
                    f'{turnament["name"]}, {turnament["date"]}, {turnament["place"]}'
                )
                print(readable, sep="\n")
        else:
            message = "Aucun tournoi dans la base de donnée."
            print(message)

    def get_all_rounds(self, Tournoi):
        if len(Tournoi.rounds_list) > 0:
            rounds_list = [r for r in Tournoi.rounds_list]
            pprint(rounds_list)
        else:
            message = "Ce tournoi ne semble pas encore avoir eu lieu et ne possède pas de tour."
            print(message)

    def get_all_matchs(self, Tournoi):
        if len(Tournoi.rounds_list) > 0:
            rounds_list = [r for r in Tournoi.rounds_list]
            matchs_list = []
            for r in rounds_list:
                matchs_list.append(r.matchs_list)
            pprint(matchs_list)
        else:
            message = "Ce tournoi ne semble pas encore avoir eu lieu et ne possède pas de match"
            print(message)
