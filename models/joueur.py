class Joueur:
    """Class for a player"""

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.name = ""
        self.birth_date = ""
        self.gender = ""
        self.rank = 0
        self.points = 0
        self.serialized = ""

    def __str__(self):
        return (
            f"{self.name} est né le {self.birth_date}, a un classement de {self.rank}."
        )

    def __repr__(self):
        return f"{self.name}, {self.birth_date}, {self.rank}"

    def update_rank(self):
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
        At the beginning of a turnament, resets the points to 0.
        """
        self.points = 0

    def serialize(self):
        self.serialized = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "rank": self.rank,
            "points": self.points,
        }

    def deserialize(self, player_db):
        self.first_name = player_db["first_name"]
        self.last_name = player_db["last_name"]
        self.name = f"{self.first_name} {self.last_name}"
        self.birth_date = player_db["birth_date"]
        self.gender = player_db["gender"]
        self.rank = int(player_db["rank"])
        self.points = int(player_db["points"])
