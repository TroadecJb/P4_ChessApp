class Turnament:
    """Class for a turnament"""

    def __init__(self, name, place, date):
        self.name = name
        self.place = place
        self.date = date
        self.number_of_rounds = 4
        self.rounds = ""
        self.players = ""
        self.time_mode = ""
        self.description = ""


class Round:
    """Class for a round"""

    def __init__(self, index, matchs_list):
        self.index = index
        self.matchs_list = matchs_list


class Match:
    """Class for a match"""

    def __init__(self, index, players_list):
        self.index = index
        self.players_list = players_list


class Player:
    """Class for a player"""

    def __init__(self, first_name, last_name, date_birth, gender, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{self.first_name} {self.last_name}"
        self.date_birth = date_birth
        self.gender = gender
        self.rank = rank
