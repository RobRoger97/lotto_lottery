# Development of ticket printing
class PrintTickets(object):
    """
        Represent the layout of the final ticket
    """
    # Maximum horizontal length of the ticket
    max_lenght = 38
    # Ticket title
    txt = "*_-_LOTTO TICKET_-_*"

    # Method that prints the top and bottom edges of tickets
    @staticmethod
    def horizontal_line():
        print('+', end="")

        for l in range (PrintTickets.max_lenght - 2):
            print('-', end="")
        print('+')

    # Method that prints double line
    @staticmethod
    def horizontal_2line():
        print('+', end="")

        for l in range (PrintTickets.max_lenght - 2):
            print('=', end="")
        print('+')

    # Method that prints a string in the center of a 
    # space as long as the max_lenght
    @staticmethod
    def central(txt=""):
        print("|",txt.center(PrintTickets.max_lenght - 4),"|")

    # Method that prints a blank line of the ticket
    @staticmethod
    def empty_line():
        print('|', end="")
        for l in range (PrintTickets.max_lenght - 2):
            print(' ', end="")
        print('|')

    @staticmethod
    def table(city,type_bill,numb):
        # String composed of the numbers extracted from 
        # the list and separated by a blank space
        string = " ".join([str(n) for n in numb])
        # Head of ticket
        PrintTickets.horizontal_line()
        PrintTickets.central(PrintTickets.txt)
        PrintTickets.horizontal_2line()
        # Body of ticket
        PrintTickets.empty_line()
        PrintTickets.central(f"CITY: {city}")
        PrintTickets.empty_line()
        PrintTickets.central(f"BET: {type_bill}")
        PrintTickets.empty_line()
        # Bottom of ticket
        PrintTickets.horizontal_2line()
        PrintTickets.central(f"{string}")
        PrintTickets.empty_line()
        PrintTickets.horizontal_line()
        print()

if __name__ == '__main__':
    lis = [10,28,39,45,54,63,72,80,90,28] # Example with max of number (10)
    test = PrintTickets()
    test.table('Napoli','cinquina', lis)  