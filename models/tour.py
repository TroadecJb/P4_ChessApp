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
        for match in self.matchs_list:
            match.__repr__()

    def starting_time(self):
        date_time = datetime.now()
        print(type(date_time))
        c = date_time.strftime("%d/%m/%Y, %H:%M%S")
        print(type(c))
        self.start_time = c

    def ending_time(self):
        time = datetime.now()

        self.end_time = time.strftime("%d/%m/%Y, %H:%M%S")
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
