from views.user_input import UserChoice
from controllers.database import DbController

user_input = UserChoice()
db_controller = DbController()


class DbViewer:
    def new_player_info(self):
        """Ask user for infos about a player, returns a list of dict with the infos."""
        new_player_list = []
        adding_entry = True

        while adding_entry:
            prompt = "\nIndiquez le nom du joueur :"
            print(prompt)
            last_name = user_input.user_input()

            prompt = "\nIndiquez le prénom du joueur :"
            print(prompt)
            first_name = user_input.user_input()

            prompt = "\nIndiquez la date de naissance (dd/mm/yyyy) :"
            print(prompt)
            birth_date = user_input.user_input()

            prompt = "\nIndiquez le classement :"
            print(prompt)
            rank = user_input.int_input()

            new_player = {
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date,
                "rank": rank,
                "points": 0,
            }
            new_player_list.append(new_player)

            prompt = "\nAjouter un autre joueur à la base de donnée ? (y/n)"
            print(prompt)
            choice = user_input.user_input()
            if choice == "y":
                adding_entry = True
            else:
                adding_entry = False

        return new_player_list
