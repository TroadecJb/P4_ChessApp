from views.database import DB_viewer
from views.rapport import Rapport
from controllers.database import Controller_db
from controllers.turnament import Tournoi_controller


class Main_menu:
    def program_selection(self):
        choice = input(
            "Que souhaitez vous faire ?\n"
            "\t1- Accéder à la base de données des joueurs\n"
            "\t2- Gérer les tournois\n"
            "\t3- Générer un rapport\n"
        )

        if self.user_input == "1":
            self.players_program()
        elif self.user_input == "2":
            self.turnament_program()
        elif self.user_input == "3":
            self.report_generator()
        else:
            pass

    def players_program(self):
        choice = input(
            "0 - Retour au menu principal"
            "1 - ajouter des joueurs à la base de données\n"
            "2 - modifier les informations des joueurs"
        )

        if choice == "1":
            new_players_list = DB_viewer.new_player_info()
            Controller_db.add_players_to_DB(new_players_list)
        elif choice == "2":
            players_to_modify = Controller_db.get_players_from_DB()
            for player in players_to_modify:
                player.update_info()
                Controller_db.update_player(player)
        elif choice == "0":
            self.program_selection

    def turnament_program(self):
        """Création d'un nouveau tournoi, exécution d'un tournoi existant, ajout d'une description à propos d'un tournoi."""
        choice = input(
            "0 - Retour au menu principal"
            "1 - Créer un nouveau tournoi"
            "2 - Tournoi déjà existant"
            "3 - Ajouter une description"
        )
        if choice == "1":
            new_turnament = Tournoi_controller.create_turnament()
        elif choice == "2":
            selected_turnament = Controller_db.retrieve_turnament()
            Controller_db.deserialize_turnament(selected_turnament)
            Tournoi_controller.run_turnament(selected_turnament)
        elif choice == "3":
            selected_turnament = Controller_db.retrieve_turnament()
            Controller_db.deserialize_turnament(selected_turnament)
            selected_turnament.add_description()
            Controller_db.update_turnament(selected_turnament)
        elif choice == "0":
            self.program_selection

    def report_generator(self):
        """Affiche différentes informations concernant la base de données (Joueurs, Tournois, Tours, Matchs)"""
        choice = input(
            "0 - Retour au menu principal"
            "1 - Afficher tous les acteurs"
            "2 - Afficher tous les tournois"
            "3 - Afficher d'autres informations sur un tournois"
        )
        if choice == "1":
            pass
        elif choice == "2":
            all_turnaments = Rapport.show_all_turnaments()
            print(all_turnaments)
        elif choice == "3":
            selected_turnament = Controller_db.retrieve_turnament()
            choice = input(
                "1 - Afficher la liste des joueurs"
                "2 - Afficher les tours"
                "3 - afficher les matchs"
                "0 - Revenir en arrière"
            )
            if choice == "1":
                players_list = Rapport.get_turnament_players(selected_turnament)
                print(players_list)
            elif choice == "2":
                rounds_list = Rapport.get_all_rounds(selected_turnament)
                print(rounds_list)
            elif choice == "3":
                matchs_list = Rapport.get_all_matchs(selected_turnament)
                print(matchs_list)
            elif choice == "0":
                self.report_generator()

        elif choice == "0":
            self.program_selection()
