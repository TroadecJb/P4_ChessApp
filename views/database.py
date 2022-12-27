class DB_viewer:
    def ask_player_info():
        last_name = input("Entrez le nom de famille du joueur :\n").lower()
        first_name = input("Entrez le prénom du joueur :\n").lower()
        birth_date = input("Entrez la date de naissance du joueur (dd/mm/yyyy) :\n")
        info = (last_name, first_name, birth_date)
        return info

    def ask_turnament_info():
        turnament_name = input("Entrez le nom du tournoi :\n").lower()
        turnament_date = input("Entrez la date du tournoi :\n").lower()
        turnament_place = input("Entrez le lieu du tournoi :\n").lower()
        info = (turnament_name, turnament_date, turnament_place)
        return info

    def new_player_info():
        new_player_list = []
        adding_entry = True

        while adding_entry:
            last_name = input("Indiquez le nom du joueur :\n").lower()
            first_name = input("Indiquez le prénom du joueur :\n").lower()
            name = f"{first_name} {last_name}"
            birth_date = input(
                f"Indiquez la date de naissance (dd/mm/yyyy) :\n"
            ).lower()
            gender = input(f"Indiquez le genre de {name} : \n").lower()
            rank = input(f"Indiquez le classement de {name} :\n").lower()

            new_player = {
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date,
                "gender": gender,
                "rank": rank,
                "points": 0,
            }
            new_player_list.append(new_player)

            prompt = input(
                "Ajouter un autre joueur à la base de donnée ? (y/n)\n"
            ).lower()
            if prompt == "y":
                adding_entry = True
            else:
                adding_entry = False

        return new_player_list
