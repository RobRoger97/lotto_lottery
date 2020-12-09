from lotto.print import Print
from lotto.ticket import Ticket
from lotto.extraction import Extraction

class Lotto(object):
    """
        Represents a bill of the lotto game.
        Attribute is:
        - ticket_amount (int)
    """

    def __init__(self, ticket_amount=0):
        self.winning_numbers = []
        self.winning_cities = []
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
    # Method that generates tickets based on the number indicated by the user
    @staticmethod
    def generate_tickets(ticket_amount):
        input_list = []
        for t in range(ticket_amount):
            Print.num_ticket(t)
            entered = Ticket.input_ticket(Ticket)
            input_list.append(entered)
        return input_list

    # Call the method to print the ticket and the method of winning
    @staticmethod
    def lotto_tickets(self,input_list,extraction):
        for en in input_list: # en = entered
            next_step = Print.next_step(Print)
            if next_step == True:
                Ticket.print_ticket(en)
                self.check_win(en[0], en[2], en[3], extraction)
                if self.winning_numbers != None and self.winning_cities != None:
                    if en[0] != "Tutte":
                        if len(self.winning_numbers) >= en[3]:
                            Print.print_winner(Print,en[0],en[1],self.winning_numbers)
                            print()
                            
                        else:
                            Print.print_loser(Print)
                            print()

                    elif en[0] == "Tutte":
                        if self.winning_numbers == [] or self.winning_cities == []:
                            Print.print_loser(Print)
                        else:
                            Print.print_winner_Tutte(Print, self.winning_numbers, self.winning_cities, en[1])
                else:
                    Print.print_loser(Print)
                    print()

    # Method that verifies the winnings
    @staticmethod
    def check_win(self, city, numbers, int_bet, extraction): #en = entered
        win_numb = []
        next_step = Print.next_step(Print)
        for key,value in extraction.cities_numbers.items():
            if city == key: ## en[0] = city
                for n in numbers: ## en[2] = list of numbers
                    if n in value:
                        win_numb.append(n)
                self.winning_numbers = win_numb                       

        if city == "Tutte":
            winning = {}
            for c in extraction.cities_numbers.keys():
                win_numb = []
                for n in numbers:
                    if n in extraction.cities_numbers[c]:
                        win_numb.append(n)
                        winning[c] = win_numb

            for c in winning.keys():
                if len(winning[c]) >= int_bet:
                    self.winning_numbers.append(winning[c])
                    
                    self.winning_cities.append(c)
                
                else:
                    pass

if __name__ == '__main__':
    ex = Lotto()
    input_list = ex.generate_tickets(2)
    ex.lotto_tickets(input_list)
