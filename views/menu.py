from P4_ChessApp.views.database_viewer import DbViewer
from views.user_input import UserChoice
from controllers.database_controller import DbController
from controllers.turnament import TournoiController
from controllers.rapport import Rapport

db_viewer = DbViewer()
rapport = Rapport()
controller_db = DbController()
tournoi_controller = TournoiController()
user_input = UserChoice()


class Main_menu:
    """Class to execute menu of program."""

    def __init__(self):
        self.active = True
        user_input.user_help()

    def program_selection(self):
        """Main menu method."""

        while self.active:
            prompt = (
                "\n- - - Menu Principal - - -\n"
                "Que souhaitez vous faire ?\n"
                "\t1- Gestion des joueurs\n"
                "\t2- Gérer les tournois\n"
                "\t3- Générer un rapport\n"
            )
            print(prompt)
            choice = user_input.str_range_input(["1", "2", "3"])

            if choice == "1":
                self.players_program()
            elif choice == "2":
                self.turnament_program()
            elif choice == "3":
                self.report_program()
            else:
                print("\tPour quitter entrer 'quitter'.")
                self.program_selection()

    def players_program(self):
        """Players programm menu."""

        while self.active:
            prompt = (
                "\n- - - Menu Principal / Gestion des joueurs - - -\n"
                "\t0 - Retour au menu principal\n"
                "\t1 - Afficher tous les joueurs\n"
                "\t2 - Ajouter des joueurs\n"
                "\t3 - Modifier les informations des joueurs\n"
                "\t4 - Supprimer des joueurs\n"
            )
            print(prompt)

            choice = user_input.str_range_input(["0", "1", "2", "3", "4"])
            if choice == "1":
                rapport.show_all_players()

            elif choice == "2":
                new_players = db_viewer.new_player_info()
                controller_db.add_players_to_db(new_players)

            elif choice == "3":
                player_to_modify = controller_db.get_one_player_from_db()
                if player_to_modify:
                    prompt = (
                        "\nSélectionner l'information à modifier:\n"
                        "\t1 - nom\n"
                        "\t2 - prénom\n"
                        "\t3 - date de naissance\n"
                        "\t4 - classement\n"
                        "\t5 - points\n"
                        "\t6 - tout\n"
                    )
                    print(prompt)
                    choice = user_input.str_range_input(["1", "2", "3", "4", "5", "6"])
                    if choice == "1":
                        print(f"\nNom du joueur: {player_to_modify.last_name}")
                        player_to_modify.set_last_name()
                    elif choice == "2":
                        print(f"\Prénom du joueur: {player_to_modify.first_name}")
                        player_to_modify.set_first_name()
                    elif choice == "3":
                        print(f"\nDate de naissance du joueur: {player_to_modify.birth_date}")
                        player_to_modify.set_birth_date()
                    elif choice == "4":
                        print(f"\nClassement du joueur: {player_to_modify.rank}")
                        player_to_modify.set_rank()
                    elif choice == "5":
                        print(f"\nPoints du joueur: {player_to_modify.points}")
                        player_to_modify.set_points()
                    elif choice == "6":
                        print(
                            f"\nInformations actuelles:"
                            f"\n{player_to_modify.last_name} {player_to_modify.first_name}"
                            f"\n{player_to_modify.birth_date}"
                            f"\nclassement: {player_to_modify.rank}, points: {player_to_modify.points}"
                        )
                        player_to_modify.update_info()
                    else:
                        pass

                    controller_db.update_player_in_db(player_to_modify)

                else:
                    pass

            elif choice == "4":
                controller_db.remove_player_in_db()

            elif choice == "0":
                self.program_selection()

    def turnament_program(self):
        """Création d'un nouveau tournoi, exécution d'un tournoi existant, ajout d'une description."""

        while self.active:
            prompt = (
                "\n- - - Menu Principal / Gestion des tournois - - -\n"
                "\t0 - Retour au menu principal\n"
                "\t1 - Créer un nouveau tournoi\n"
                "\t2 - lancer tournoi\n"
                "\t3 - Ajouter une description\n"
                "\t4 - Modifier tournoi\n"
                "\t5 - Supprimer un tournoi\n"
            )
            print(prompt)
            choice = user_input.str_range_input(["0", "1", "2", "3", "4", "5"])
            if choice == "1":
                new_turnament = tournoi_controller.create_turnament()
                if new_turnament:
                    controller_db.save_turnament(new_turnament)
                else:
                    pass

            elif choice == "2":
                selected_turnament = controller_db.retrieve_turnament()
                if selected_turnament:
                    selected_turnament = controller_db.deserialize_turnament(
                        selected_turnament
                    )

                    tournoi_controller.run_turnament(selected_turnament)
                else:
                    pass

            elif choice == "3":
                selected_turnament = controller_db.retrieve_turnament()
                if selected_turnament:
                    selected_turnament = controller_db.deserialize_turnament(
                        selected_turnament
                    )
                    selected_turnament.add_description()
                    controller_db.update_turnament(selected_turnament)
                else:
                    pass

            elif choice == "4":  # submenu to choose which types of information
                turnament_to_modify = controller_db.retrieve_turnament()
                if turnament_to_modify:
                    turnament_to_modify = controller_db.deserialize_turnament(
                        turnament_to_modify
                    )
                    prompt = (
                        "\nSélectionner l'information à modifier:\n"
                        "\t1 - Nom\n"
                        "\t2 - Date\n"
                        "\t3 - Lieu\n"
                        "\t4 - Mode de controle de temps\n"
                        "\t5 - Nombre de tours\n"
                        "\t6 - Liste des joueurs\n"
                        "\t7 - Modifier la description\n"
                        "\t8 - Toutes les informations\n"
                    )
                    print(prompt)
                    choice = user_input.str_range_input(
                        ["1", "2", "3", "4", "5", "6", "7", "8"]
                    )
                    if choice == "1":
                        turnament_to_modify.set_name()
                    elif choice == "2":
                        turnament_to_modify.set_date()
                    elif choice == "3":
                        turnament_to_modify.set_place()
                    elif choice == "4":
                        turnament_to_modify.set_time_control()
                    elif choice == "5":
                        turnament_to_modify.set_number_rounds()
                    elif choice == "6":   # submenu to choose which types of information
                        prompt = (
                            "\nModification de la liste des joueurs\n"
                            "\t1 - Ajouter des joueurs\n"
                            "\t2 - Retier des joueurs\n"
                        )
                        print(prompt)
                        choice = user_input.str_range_input(["1", "2"])
                        tournoi_controller.modify_players_list(
                            turnament_to_modify, choice
                        )
                    elif choice == "7":
                        turnament_to_modify.add_description()
                    elif choice == "8":
                        turnament_to_modify.update_info()
                    controller_db.update_turnament(turnament_to_modify)

            elif choice == "5":
                controller_db.remove_turnament_in_db()
            elif choice == "0":
                self.program_selection()

    def report_program(self):
        """Affiche différentes informations concernant la base de données (Joueurs, Tournois, Tours, Matchs)"""

        while self.active:
            prompt = print(
                "\n- - - Menu Principal / Rapports - - -\n"
                "\t0 - Retour au menu principal\n"
                "\t1 - Afficher la liste de tous les joueurs\n"
                "\t2 - Afficher tous les tournois\n"
                "\t3 - Afficher d'autres informations sur un tournoi\n"
            )
            choice = user_input.str_range_input(["0", "1", "2", "3"])

            if choice == "1":
                rapport.show_all_players()

            elif choice == "2":
                rapport.show_all_turnaments()

            elif choice == "3":  # submenu to choose which types of information
                selected_turnament = controller_db.retrieve_turnament()
                if selected_turnament:
                    selected_turnament = controller_db.deserialize_turnament(
                        selected_turnament
                    )
                    prompt = (
                        "\n- - - Menu Principal / Rapports / Autres information du tournoi - - -\n"
                        "\t0 - Revenir en arrière\n"
                        "\t1 - Afficher la liste des joueurs\n"
                        "\t2 - Afficher les tours\n"
                        "\t3 - afficher les matchs\n"
                    )
                    print(prompt)
                    choice = user_input.str_range_input(["0", "1", "2", "3"])
                    if choice == "1":
                        rapport.show_turnament_players(selected_turnament)

                    elif choice == "2":
                        rapport.show_turnament_rounds(selected_turnament)

                    elif choice == "3":
                        rapport.show_turnament_matchs(selected_turnament)

                    elif choice == "0":
                        self.report_program()
                else:
                    print("Pas de tournoi dans la base de donnée.")

            elif choice == "0":
                self.program_selection()
