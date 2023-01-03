from views.database import DB_viewer
from views.rapport import Rapport
from controllers.database import Controller_db
from controllers.turnament import Tournoi_controller

db_viewer = DB_viewer()
rapport = Rapport()
controller_db = Controller_db()
tournoi_controller = Tournoi_controller()


class Main_menu:
    def __init__(self):
        self.active = True

    def user_input(self):
        user_input = input()
        if user_input == "quitter":
            quit()
        else:
            return user_input

    def program_selection(self):
        while self.active:
            prompt = print(
                "\nQue souhaitez vous faire ?\n"
                "\t1- Accéder à la base de données des joueurs\n"
                "\t2- Gérer les tournois\n"
                "\t3- Générer un rapport\n"
            )
            choice = self.user_input()

            if choice == "1":
                self.players_program()
            elif choice == "2":
                self.turnament_program()
            elif choice == "3":
                self.report_generator()
            else:
                print("\tPour quitter entrer 'quitter'.")
                self.program_selection()

    def players_program(self):
        while self.active:
            prompt = print(
                "\nBase de données des joueurs\n"
                "\t0 - Retour au menu principal\n"
                "\t1 - ajouter des joueurs à la base de données\n"
                "\t2 - modifier les informations des joueurs\n"
            )
            choice = self.user_input()
            if choice == "1":
                new_players = db_viewer.new_player_info()
                controller_db.add_players_to_DB(new_players)
            elif choice == "2":
                players_to_modify = controller_db.get_players_from_DB()
                for player in players_to_modify:
                    player.update_info()
                    controller_db.update_player(player)
            elif choice == "0":
                self.program_selection()

    def turnament_program(self):
        """Création d'un nouveau tournoi, exécution d'un tournoi existant, ajout d'une description à propos d'un tournoi."""
        while self.active:
            prompt = print(
                "\nGestion des tournois\n"
                "\t0 - Retour au menu principal\n"
                "\t1 - Créer un nouveau tournoi\n"
                "\t2 - Tournoi déjà existant\n"
                "\t3 - Ajouter une description\n"
            )
            choice = self.user_input()
            if choice == "1":
                new_turnament = tournoi_controller.create_turnament()
                controller_db.save_turnament(new_turnament)
            elif choice == "2":
                selected_turnament = controller_db.retrieve_turnament()
                controller_db.deserialize_turnament(selected_turnament)
                tournoi_controller.run_turnament(selected_turnament)
            elif choice == "3":
                selected_turnament = controller_db.retrieve_turnament()
                controller_db.deserialize_turnament(selected_turnament)
                selected_turnament.add_description()
                controller_db.update_turnament(selected_turnament)
            elif choice == "0":
                self.program_selection()

    def report_generator(self):
        """Affiche différentes informations concernant la base de données (Joueurs, Tournois, Tours, Matchs)"""
        while self.active:
            prompt = print(
                "\nRapports\n"
                "\t0 - Retour au menu principal\n"
                "\t1 - Afficher tous les acteurs\n"
                "\t2 - Afficher tous les tournois\n"
                "\t3 - Afficher d'autres informations sur un tournois\n"
            )
            choice = self.user_input()

            if choice == "1":
                pass
            elif choice == "2":
                all_turnaments = rapport.show_all_turnaments()
                print(all_turnaments)
            elif choice == "3":
                selected_turnament = controller_db.retrieve_turnament()
                selected_turnament = controller_db.deserialize_turnament(
                    selected_turnament
                )
                prompt = print(
                    "\nAutres informations tournoi\n"
                    "\t1 - Afficher la liste des joueurs\n"
                    "\t2 - Afficher les tours\n"
                    "\t3 - afficher les matchs\n"
                    "\t0 - Revenir en arrière\n"
                )
                choice = self.user_input()
                if choice == "1":
                    players_list = rapport.get_turnament_players(selected_turnament)
                    print(players_list)
                elif choice == "2":
                    rounds_list = rapport.get_all_rounds(selected_turnament)
                    print(rounds_list)
                elif choice == "3":
                    matchs_list = Rapport.get_all_matchs(selected_turnament)
                    print(matchs_list)
                elif choice == "0":
                    self.report_generator()

            elif choice == "0":
                self.program_selection()
