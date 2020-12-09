class Print(object):
    """
        Represent the layout
    """

    max_lenght = 50
    # Method that prints the top and bottom edges of tickets
    @staticmethod
    def horizontal_line():
        print('+', end="")

        for l in range (Print.max_lenght - 2):
            print('-', end="")
        print('+')

    # Method that prints double line
    @staticmethod
    def horizontal_2line():
        print('+', end="")

        for l in range (Print.max_lenght - 2):
            print('=', end="")
        print('+')

    # Method that prints a string in the center of a 
    # space as long as the max_lenght
    @staticmethod
    def central(txt=""):
        print("|",txt.center(Print.max_lenght - 4),"|")

    # Method that prints a blank line of the ticket
    @staticmethod
    def empty_line():
        print('|', end="")
        for l in range (Print.max_lenght - 2):
            print(' ', end="")
        print('|')

    # Indicates the number of the ticket to be filled
    @staticmethod
    def num_ticket(num):
        print()
        print(f"TICKET {num+1}:")
        print()

    # Gives the command to the user to go to the next step
    @staticmethod
    def next_step(self):
        self.horizontal_2line()
        self.central("Press a key for the next step.")
        self.horizontal_2line() 
        next_step = input("")
        print()
        return True

    # Printing of the winning ticket
    def print_winner(self,city,bet,numbers):
        self.horizontal_line()
        self.central("!!YOUR TICKET IS A WINNER!!")
        self.horizontal_2line()
        self.central("RUOTA {}".format(city))
        self.central("With {} on the numbers:".format(bet))
        # Turn numbers into a string, separated by spaces
        string = " ".join([str(y) for y in numbers])
        self.central(f"{string}")
        self.horizontal_2line()

    # # Printing of the loser ticket
    def print_loser(self):
        self.horizontal_line()
        self.central("!!IT WILL BE FOR THE NEXT ONE!!")
        self.horizontal_2line()
        self.central("The ticket isn't winning...")
        self.horizontal_2line()

    # Printing of the winning ticket (if "Tutte" is chosen)
    def print_winner_Tutte(self, numbers, cities, bet):
        self.horizontal_line()
        self.central("!!YOUR TICKET IS A WINNER!!")
        self.horizontal_2line()
        self.empty_line()
        # Print loop of each city's winnings
        for i in range(0,len(cities)):
            self.central("RUOTA {}".format(cities[i]))
            self.central("With {} on the numbers:".format(bet))
            # Turn numbers into a string, separated by spaces
            string = " ".join([str(y) for y in numbers[i]])
            self.central(f"{string}")
            self.empty_line()
        self.horizontal_2line()