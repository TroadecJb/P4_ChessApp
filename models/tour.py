from datetime import datetime


class Tour:
    """Class for a round"""

    def __init__(self, index):
        self.index = index
        self.matchs_list = []
        self.start_time = ""
        self.end_time = ""
        self.serialized = {
            "round_index": self.index,
            "matchs_list": "",
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    def __repr__(self):
        return f"Tour {self.index}, liste des matchs: {self.matchs_list}, début: {self.start_time}, fin: {self.end_time}."

    def start_round(self):
        self.start_time = datetime.now()

    def end_round(self):
        self.end_time = datetime.now()

    def serialize(self):
        readable_match = [match.serialized for match in self.matchs_list]
        # a dégager si la liste de compréhension au dessus fonctionne
        readable = []
        for match in matchs_list:
            match.serialize()
            readable.append(match.serialized)

        self.serialized = {
            "round_index": self.index,
            "matchs_list": readable_match,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
