class UserChoice:
    """Check for user input."""

    def __init__(self):
        self.message = "Veuillez entrer un nombre parmi ceux proposés.\n"

    def user_input(self):
        choice = input()
        if choice.lower() == "quitter":
            quit()
        elif choice.lower() == "annuler":
            pass
        else:
            return choice.lower()

    def int_input(self):
        """Check if user input is type(int). Returns input type(int)."""
        choice = self.user_input()
        if choice:
            try:
                int_choice = int(choice)
            except ValueError:
                print("Veuillez entrer un nombre.")
                return self.int_input()
            return int_choice
        else:
            return

    def float_input(self):
        """Check if user input is type(int). Returns input type(int)."""
        choice = self.user_input()
        if choice:
            try:
                float_choice = float(choice)
            except ValueError:
                print("Veuillez entrer un nombre.")
                return self.float_input()
            return float_choice
        else:
            return

    def int_range_input(self, range):
        """Check if user input is type(int) and in range. Returns input type(int)."""
        choice = self.int_input()
        if choice:
            if choice in range:
                return choice
            else:
                print(self.message)
                return self.int_range_input(range)
        else:
            return

    def str_range_input(self, range):
        """Check if user input is in range."""
        choice = self.user_input()
        if choice:
            if choice in range:
                return choice
            else:
                print(self.message)
                return self.str_range_input()
        else:
            return
