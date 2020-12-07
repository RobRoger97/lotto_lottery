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

    @staticmethod
    def num_ticket(num):
        print()
        print(f"TICKET {num+1}:")
        print()

    @staticmethod
    def next_step(self):
        self.horizontal_2line()
        self.central("Press a key for the next step.")
        self.horizontal_2line() 
        next_step = input("")
        print()
        return True