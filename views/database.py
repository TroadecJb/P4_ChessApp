from views.user_input import UserChoice

user_input = UserChoice()


class DbViewer:
    # def ask_player_info(self):
    #     last_name = input("Entrez le nom de famille du joueur :\n").lower()
    #     first_name = input("Entrez le prénom du joueur :\n").lower()
    #     birth_date = input("Entrez la date de naissance du joueur (dd/mm/yyyy) :\n")
    #     info = (last_name, first_name, birth_date)
    #     return info

    # def ask_turnament_info(self):
    #     turnament_name = input("Entrez le nom du tournoi :\n").lower()
    #     turnament_date = input("Entrez la date du tournoi :\n").lower()
    #     turnament_place = input("Entrez le lieu du tournoi :\n").lower()
    #     info = (turnament_name, turnament_date, turnament_place)
    #     return info

    def new_player_info(self):
        """Ask user for infos about a player, returns a dict with the infos."""
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
