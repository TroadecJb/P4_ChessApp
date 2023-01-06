class User_choice:
    """Check for user input."""

    def __init__(self):
        self.message = "Veuillez entrer un nombre parmi ceux proposés.\n"

    def user_input(self):
        choice = input()
        if choice.lower() == "quitter":
            quit()
        else:
            return choice.lower()

    def int_input(self):
        """Check if user input is type(int). Returns input type(int)."""
        choice = self.user_input()
        try:
            int_choice = int(choice)
        except ValueError:
            print("Veuillez entrer un nombre.")
            self.int_input()
        return int_choice

    def int_range_input(self, range):
        """Check if user input is type(int) and in range. Returns input type(int)."""
        choice = self.int_input()
        if choice in range:
            return choice
        else:
            print(self.message)
            self.int_range_input()

    def str_range_input(self, range):
        """Check if user input is in range."""
        choice = self.user_input()
        if choice in range:
            return choice
        else:
            print(self.message)
            self.str_range_input()
