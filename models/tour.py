from datetime import datetime


class Tour:
    """Class for a round"""

    def __init__(self, index):
        self.index = index
        self.matchs_list = []
        self.start_time = ""
        self.end_time = ""

    def __repr__(self):
        matchs = [str(m) for m in self.matchs_list]
        message = (
            f"\nTour {self.index}\n"
            f"début: {self.start_time}\n"
            f"fin: {self.end_time}\n"
            "Liste des matchs:\n"
        )
        return message + "\n".join(matchs)
    def show_matchs(self):
        for match in self.matchs_list:
            match.__repr__()

    def starting_time(self):
        """Record the date and time at the beginning of the round."""

        date_time = datetime.now()
        self.start_time = date_time.strftime("%d/%m/%Y, %H:%M:%S")

    def ending_time(self):
        """Record the date and time at the end of the round."""
        date_time = datetime.now()

        self.end_time = date_time.strftime("%d/%m/%Y, %H:%M:%S")
        for match in self.matchs_list:
            match.set_result()

    def serialize(self):
        """Serialize informations of Tour."""

        matchs_list = []
        for match in self.matchs_list:
            x = match.serialize()
            matchs_list.append(x)

        serialized = {
            "index": self.index,
            "matchs_list": matchs_list,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
        return serialized

    def deserialize(self, data):
        """Deserialize informations of Tour."""

        self.matchs_list = data["matchs_list"]
        self.start_time = data["start_time"]
        self.end_time = data["end_time"]
