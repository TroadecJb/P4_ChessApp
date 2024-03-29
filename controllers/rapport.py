from tinydb import TinyDB
import operator
from views.user_input import UserChoice

DB = TinyDB("db.json")
JOUEUR_TABLE = DB.table("joueurs")
TOURNOI_TABLE = DB.table("tournois")

user_input = UserChoice()


class Rapport:
    """Class that generates reports to show user several types of informations."""

    def show_all_players(self):
        """Print informations of every players in database table."""

        players_list = JOUEUR_TABLE.all()
        if players_list:
            prompt = "Sélectionner le rangement  1- alphabétique | 2- classement\n"
            print(prompt)
            
            choice = user_input.str_range_input(["1", "2"])
            if choice == "1":
                liste = sorted(
                    players_list, key=operator.itemgetter("last_name")
                )
            elif choice == "2":
                liste = sorted(
                    players_list, key=operator.itemgetter("rank"), reverse=True
                )
            
            message = (
                "\nListe des joueurs :\n"
                "Nom / Prénom / Classement\n"
            )
            print(message)
            for player in liste:
                print(f'{player["last_name"]} {player["first_name"]}, {player["rank"]}')

        else:
            print("Aucun joueur dans la base donnée.")
            pass

    def show_turnament_players(self, Tournoi):
        """Print informations of every players in a turnament."""

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
        """Print informations of every turnament in database tournoi."""

        turnament_data = TOURNOI_TABLE.all()
        if turnament_data:
            prompt = "\nListe des tournois:"
            print(prompt)
            for turnament in turnament_data:
                readable = (
                    f'{turnament["name"]}, {turnament["date"]}, {turnament["place"]}'
                    f'\ndescription: {turnament["description"]}\n'
                )
                print(readable, sep="\n")
        else:
            message = "Aucun tournoi dans la base de donnée."
            print(message)
            pass

    def show_turnament_rounds(self, Tournoi):
        """Print informations of every rounds in a turnament."""

        if len(Tournoi.rounds_list) > 0:
            rounds_list = [r for r in Tournoi.rounds_list]
            for r in rounds_list:
                print(r)
        else:
            message = "Ce tournoi ne semble pas encore avoir eu lieu et ne possède pas de tour."
            print(message)

    def show_turnament_matchs(self, Tournoi):
        """Print informations of every matchs in a turnament."""

        if len(Tournoi.rounds_list) > 0:
            rounds_list = [r for r in Tournoi.rounds_list]
            for r in rounds_list:
                for m in r.matchs_list:
                    print(m)
        else:
            message = "Ce tournoi ne semble pas encore avoir eu lieu et ne possède pas de match"
            print(message)
