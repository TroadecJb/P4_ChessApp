from views.user_input import UserChoice

user_input = UserChoice()


class Joueur:
    """Class for a player"""

    def __init__(self):
        self.doc_id = ""
        self.first_name = ""
        self.last_name = ""
        self.birth_date = ""
        self.rank = 0
        self.points = 0
        self.serialized = ""

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}, {self.birth_date}, rank: {self.rank}, points: {self.points}"

    def update_rank(self):  # A deplacer dans le controleur DB
        current_rank = self.rank
        print(f"{self.name}, classement actuel : {current_rank}")
        prompt = input(f"Mettre à jour le classement de {self.name} ? (y/n)\n").lower()
        if prompt == "y":
            new_rank = float(input("Indiquez le nouveau classement de {self.name} :\n"))
            self.rank = new_rank
        else:
            pass

    def reset_points(self):
        """
        The points allows to know how to update the rank of the player at the end of the turnament.
        In the beginning of a new turnament, resets the points to 0.
        """
        self.points = 0

    def serialize(self):
        self.serialized = {
            "doc_id": self.doc_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "rank": self.rank,
            "points": self.points,
        }
        return self.serialized

    def deserialize(self, player_db):
        self.doc_id = player_db.doc_id
        self.first_name = player_db["first_name"]
        self.last_name = player_db["last_name"]
        self.name = f"{self.first_name} {self.last_name}"
        self.birth_date = player_db["birth_date"]
        self.rank = int(player_db["rank"])
        self.points = int(player_db["points"])

    def update_info(self):
        self.set_first_name()
        self.set_last_name()
        self.set_birth_date()
        self.set_rank()
        self.set_points()

    def set_first_name(self):
        prompt = "\nEntrez le prénom du joueur:"
        print(prompt)
        player_fisrt_name = user_input.user_input()
        self.first_name = player_fisrt_name

    def set_last_name(self):
        prompt = "\nEntrez le nom du joueur :"
        print(prompt)
        player_last_name = user_input.user_input()
        self.last_name = player_last_name

    def set_birth_date(self):
        prompt = "\nEntrez la date de naissance du joueur (dd/mm/yyyy):"
        print(prompt)
        player_birth_date = user_input.user_input()
        self.birth_date = player_birth_date

    def set_rank(self):
        prompt = "\nEntrez le classement du joueur :"
        print(prompt)
        player_rank = user_input.int_input()
        self.rank = player_rank

    def set_points(self):
        prompt = "\nEntrez les points du joueur:"
        print(prompt)
        player_points = user_input.int_input()
        self.points = player_points
