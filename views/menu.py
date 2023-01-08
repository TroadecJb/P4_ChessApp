from views.database import DbViewer
from views.rapport import Rapport
from views.user_input import UserChoice
from controllers.database import ControllerDb
from controllers.turnament import TournoiController

db_viewer = DbViewer()
rapport = Rapport()
controller_db = ControllerDb()
tournoi_controller = TournoiController()
user_input = UserChoice()


class Main_menu:
    def __init__(self):
        self.active = True

    def program_selection(self):
        while self.active:
            prompt = print(
                "\n- - - Menu Principal - - -\n"
                "Que souhaitez vous faire ?\n"
                "\t1- Gestion des joueurs\n"
                "\t2- Gérer les tournois\n"
                "\t3- Générer un rapport\n"
            )
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
                controller_db.add_players_to_DB(new_players)

            elif choice == "3":
                player_to_modify = controller_db.get_player_from_DB()

                prompt = (
                    "Sélectionner l'information à modifier:\n"
                    "\t1 - nom\n"
                    "\t2 - prénom\n"
                    "\t3 - date de naissance\n"
                    "\t4 - classement\n"
                    "\t5 - points\n"
                    "\t6 - tout\n"
                )
                print(prompt)
                choice = user_input.user_input()
                if choice == "1":
                    player_to_modify.set_last_name()
                elif choice == "2":
                    player_to_modify.set_first_name()
                elif choice == "3":
                    player_to_modify.set_birth_date()
                elif choice == "4":
                    player_to_modify.set_rank()
                elif choice == "5":
                    player_to_modify.set_points()
                elif choice == "6":
                    player_to_modify.update_info()
                else:
                    pass
                controller_db.update_player(player_to_modify)

            elif choice == "4":
                controller_db.remove_player()

            elif choice == "0":
                self.program_selection()

    def turnament_program(self):
        """Création d'un nouveau tournoi, exécution d'un tournoi existant, ajout d'une description à propos d'un tournoi."""
        while self.active:
            # modifier le menu tournoi pour avoir: création tournoi, lancer tournoi, modifier tournoi, supprimer tournoi
            prompt = print(
                "\n- - - Menu Principal / Gestion des tournois - - -\n"
                "\t0 - Retour au menu principal\n"
                "\t1 - Créer un nouveau tournoi\n"
                "\t2 - lancer tournoi\n"
                "\t3 - Ajouter une description\n"
                "\t4 - Supprimer un tournoi\n"
            )
            choice = user_input.str_range_input(["0", "1", "2", "3", "4"])
            if choice == "1":
                new_turnament = tournoi_controller.create_turnament()
                controller_db.save_turnament(new_turnament)
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
            elif choice == "4":
                controller_db.remove_turnament()
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
                "\t3 - Afficher d'autres informations sur un tournois\n"
            )
            choice = user_input.str_range_input(["0", "1", "2", "3"])
            if choice == "1":
                rapport.show_all_players()
            elif choice == "2":
                rapport.show_all_turnaments()
            elif choice == "3":
                selected_turnament = controller_db.retrieve_turnament()
                if selected_turnament:
                    selected_turnament = controller_db.deserialize_turnament(
                        selected_turnament
                    )
                    prompt = print(
                        "\n- - - Menu Principal / Rapports / Autres information du tournoi - - -\n"
                        "\t1 - Afficher la liste des joueurs\n"
                        "\t2 - Afficher les tours\n"
                        "\t3 - afficher les matchs\n"
                        "\t0 - Revenir en arrière\n"
                    )
                    choice = self.user_input()
                    if choice == "1":
                        rapport.get_turnament_players(selected_turnament)

                    elif choice == "2":
                        rapport.get_all_rounds(selected_turnament)

                    elif choice == "3":
                        rapport.get_all_matchs(selected_turnament)

                    elif choice == "0":
                        self.report_generator()

            elif choice == "0":
                self.program_selection()
