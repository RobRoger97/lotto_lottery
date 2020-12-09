from lotto.print_tickets import PrintTickets
from lotto.input import Input

class Ticket(object):
    """
        Represents a ticket of the lotto game.
        Attributes are:
        - city (string)
        - bet  (string)
        - num  (list of random number)
    """
    def __init__(self, city ='', bet ='',num =[]):
        self.city = city
        self.bet = bet
        self.num = num
        self.int_bet = 0

    # Take the inputs from the Input class and puts them in a list
    def input_ticket(self):
        entered = []
        Input.city_user(self)
        entered.append(self.city)
        Input.type_user(self)
        entered.append(self.bet)
        Input.number_user(self)
        entered.append(self.num)
        entered.append(self.int_bet)
        return entered

    # Print the ticket with the elements of the input list
    @staticmethod
    def print_ticket(list_en):
        PrintTickets.table(list_en[0],list_en[1],list_en[2])        

if __name__ == '__main__':
    ex = Ticket()
    entered = ex.input_ticket()
    ex.print_ticket(entered)
