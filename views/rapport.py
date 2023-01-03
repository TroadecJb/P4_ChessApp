from tinydb import TinyDB, Query, where
import operator

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")


class Rapport:
    def __init__(self):
        SORTING_LIST = ("alpha", "rank")

    def print_report(self, liste):
        for item in liste:
            readable = ""

    def get_turnament_players(self, Tournoi):
        sorting_choice = input(
            "Sélectionner le rangement  1- alphabétique | 2- classement"
        )
        if sorting_choice == "1":
            liste = sorted(Tournoi.players_list, key=operator.attrgetter("name"))
        elif sorting_choice == "2":
            liste = sorted(Tournoi.players_list, key=operator.attrgetter("rank"))

        return liste

    def show_all_turnaments(
        self,
    ):
        liste = []
        turnament_data = TOURNOI_TABLE.all()
        for turnament in turnament_data:
            readable = f'{turnament["name"]}, {turnament["date"]}, {turnament["place"]}'
            liste.append(readable)

        return liste

    def get_all_rounds(self, Tournoi):
        rounds_list = [r for r in Tournoi.rounds_list]

        return rounds_list

    def get_all_matchs(self, Tournoi):
        rounds_list = self.get_all_rounds(Tournoi)
        liste = []
