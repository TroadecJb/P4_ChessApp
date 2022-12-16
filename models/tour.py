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

    def show_matchs(self):
        for match in match_list:
            match.__repr__()

    def start_time(self):
        self.start_time = datetime.now()

    def end_time(self):
        self.end_time = datetime.now()
        for match in self.matchs_list:
            match.set_result()

    def serialize(self):
        matchs_list = [match.serialize() for match in self.matchs_list]

        self.serialized = {
            "round_index": self.index,
            "matchs_list": matchs_list,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

        return self.serialized

    def deserialize(self, data):
        # self.index = data["index"]
        self.matchs_list = data["matchs_list"]
        self.start_time = data["start_time"]
        self.end_time = data["end_time"]
