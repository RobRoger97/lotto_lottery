from lotto.print import Print
from lotto.ticket import Ticket

class Lotto(object):
    """
        Represents a bill of the lotto game.
        Attribute is:
        - ticket_amount (int)
    """

    def __init__(self, ticket_amount=0):
        # Call the method that checks the validity of the ticket_amount
        if Lotto.is_ticket_amount_valid(ticket_amount):
            self.ticket_amount = ticket_amount
        else:
            pass

    # Check that the number of tickets entered is valid
    @staticmethod
    def is_ticket_amount_valid(ticket_amount):
        if ticket_amount >= 1 and ticket_amount <=5:
            return True
        else:
            return False
    
    @staticmethod
    def generate_tickets(self, ticket_amount):
        input_list = []
        for t in range(ticket_amount):
            Print.num_ticket(t)
            entered = Ticket.input_ticket(self)
            input_list.append(entered)
        return input_list

    @staticmethod
    def print_all_tickets(input_list):
        next_step = Print.next_step(Print)
        if next_step == True:
            for en in input_list:
                Ticket.print_ticket(en)

            
if __name__ == '__main__':
    ex = Lotto()
    input_list = ex.generate_tickets(ex,2)
    ex.print_all_tickets(input_list)