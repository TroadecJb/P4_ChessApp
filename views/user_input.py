class User_input:
    """Check for user input."""

    def int_input(self):
        """Check if user input is type(int). Returns input type(int)."""
        choice = input()
        try:
            int_choice = int(choice)
        except ValueError:
            print("Veuillez entrer un nombre.")
            self.int_input()
        return int_choice

    def in_range_input(self, range):
        """Check if user input is type(int) and in range. Returns input type(int)."""
        choice = self.int_input()
        try:
            choice in range
        except ValueError:
            print("Veuillez entrer un nombre parmi ceux proposés.")
            self.in_range_input()
        return choice
