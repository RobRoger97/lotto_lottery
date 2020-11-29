from random import randrange
# Import methods from other files
from lotto.city import City
from lotto.type_of_bill import TypeBill
from lotto.prints import PrintTickets
from lotto.extraction import Extraction
from lotto.prizes import Prize

class Lotto(object):

    """
        Represents a bill of the lotto game.
        Attributes are:
        - city (string)
        - bet  (string)
        - num  (list of random number)
        - ticket_amount (int)
    """
    def __init__(self, city ='', bet ='',num =[], ticket_amount=0, play = '0'):
        self.city = city
        self.bet = bet
        self.num = num
        self.int_bet = 0
        self.win_num = []
        self.play = play
        # Call the method that checks the validity of the ticket_amount
        if Lotto.is_ticket_amount_valid(ticket_amount):
            self.ticket_amount = ticket_amount
        else:
            pass
    
    # Method in which the user is asked to enter the number 
    # of random numbers to play
    def number_user(self):
        max_num = 10 # Maximum number to respect

        while True:            
            amount = input("How many numbers? \n \
                        Enter a number from 1 to 10\n \
                        ---> ")
            # Case in which the user does not enter a number           
            if amount.isdigit()== False:
                print("This is not a number!")
                print("Please, try again...")
                print()
            else:
                if int(amount) >= self.int_bet and int(amount) <= max_num:
                    self.num = Lotto.random_numbers(int(amount))
                    break
                # If it is a number, we have to handle the errors 
                # in this case as well
                elif int(amount) < self.int_bet: # The type of bill must also be considered
                    print("The number entered is too low")
                    print("Please, try again...")
                    print()

                elif int(amount) > 10:
                    print("The number entered is out of range")
                    print("Please, try again...")
                    print()
                

    # Method in which the user is asked to enter the city
    def city_user(self):
        PrintTickets.horizontal_line()
        txt = "Choose one of the next cities"
        PrintTickets.central(txt)
        PrintTickets.horizontal_under()
        # Creates a list of cities to observe from for the user can choose
        for x,name in enumerate(City.cities_list,1):
            print("%2.0f)"%(x), " ", name)
        
        PrintTickets.horizontal_line()

        while True:
            user_city = input("Enter the name of the city: ")
            # The method is called to verify that the city is valid
            if City.is_city_valid(user_city):
                c = City(user_city)
                self.city = c.city
                break
            elif user_city.isdigit(): # Case in which the user enter a number
                print("Enter the name of the city,\n "\
                    "not the number!")
                print("Please, try again...")
                print()

    # Method in which the user is asked to enter the type of bill           
    def type_user(self):
        PrintTickets.horizontal_line()
        txt = "Choose one of the next type of bill:"
        PrintTickets.central(txt)
        PrintTickets.horizontal_under()
         # Creates a list of type to observe from for the user can choose
        for x,name in enumerate(TypeBill.types_list,0):
            if name!=None:
                print("%2.0f)"%(x), " ", name)
        PrintTickets.horizontal_line()

        while True:
            user_type = input("Enter the type of bill: ")
            # The method is called to verify that the type is valid
            if TypeBill.is_bill_valid(user_type): 
                b = TypeBill(user_type)
                self.int_bet = b.min_num
                self.bet = b.bill_type
                
                break
            elif user_type.isdigit(): # Case in which the user enter a number
                print("Enter the type of bill,\n" \
                    "not the number!")
                print("Please, try again...")
                print()

    # Method that takes the number entered by the user as an argument 
    # and creates lists of random numbers
    @staticmethod
    def random_numbers(number_amount):
        num_list = []
        for n in range(number_amount):
            num = randrange(1,90+1)

            while True:
                if num in num_list: # If the number exists, repeat..
                    num = randrange(1,90+1)
                else:
                    break
            num_list.append(num)
        return num_list

    # Check that the number of tickets entered is valid
    @staticmethod
    def is_ticket_amount_valid(ticket_amount):
        if ticket_amount >= 1 and ticket_amount <=5:
            return True
        else:
            return False

    #method that uses the previous methods to print 1 to n tickets 
    # requested by the user        
    @staticmethod
    def print_ticket(self,ticket_amount):
        # Dictionary containing all cities, bet types, numbers, int_bet and played  
        # entered by the user
        dic = {'city' : [], 'bet' : [], 'num' : [], 'int_bet': [], 'played': []}
        # Recall of methods for each ticket
        for t in range(ticket_amount):
            print()
            print(f"TICKET {t+1}:")
            print()
            Lotto.city_user(self)
            dic['city'].append(self.city)
            Lotto.type_user(self)
            dic['bet'].append(self.bet)
            dic['int_bet'].append(self.int_bet)
            Lotto.number_user(self)
            dic['num'].append(self.num)
            Lotto.play_user(self)
            dic['played'].append(self.play)
        extr = Extraction()
        extr.print_extraction()
        # Printing of individual tickets
        for t in range(ticket_amount):    
            cit = dic['city']
            type_bill = dic['bet']
            num = dic['num']
            int_b = dic['int_bet']
            play_us = dic['played']
            PrintTickets.table(cit[t],type_bill[t],num[t],play_us[t])
            # Verify the winnings
            self.win_num = extr.is_winner(cit[t],num[t])
            # The number of numbers must be greater than the bet value
            if self.win_num != None and len(self.win_num) >= int_b[t]:
                    PrintTickets.horizontal_line()
                    PrintTickets.central("!!YOUR TICKET IS A WINNER!!")
                    PrintTickets.horizontal_under()
                    PrintTickets.central("RUOTA {}".format(cit[t]))
                    PrintTickets.central("With {} on the numbers:".format(type_bill[t]))
                    # Turn numbers into a string, separated by spaces
                    string = " ".join([str(y) for y in self.win_num])
                    PrintTickets.central(f"{string}")
                    PrintTickets.horizontal_under()
                    # Calculation of the price to be dedicated to each ticket
                    prizes = Prize()
                    combination = prizes.calculate_comb(int_b[t],self.win_num)
                    amount = prizes.calculate_amount(int_b[t],self.win_num)
                    # 8% tax
                    tax = 0.08
                    # Payout calculation
                    win = play_us[t]*combination*amount
                    # If less than 500 it does not consider the tax
                    if win <= 500:
                        if cit[t] == "Tutte": # If "Tutte" the payout is divided by 10
                            win/=10
                        PrintTickets.horizontal_line()
                        PrintTickets.central("TOTAL WIN: {:.2f}€".format(win))
                        PrintTickets.horizontal_under()
                    # If greater than 500, gross and net must be considered
                    else:
                        net_win = win-(win*tax)
                        if win > 6000000:
                            net_win = 6000000 # For each ticket the maximum profit is 6,000,000
                        if cit[t] == "Tutte":
                            net_win/=10
                        PrintTickets.horizontal_line()
                        PrintTickets.central("GROSS WIN: {:.2f}€".format(win))
                        PrintTickets.central("NET WIN: {:.2f}€".format(net_win))
                        PrintTickets.horizontal_under()
            # If the ticket is not winning
            else:   
                    PrintTickets.horizontal_line()
                    PrintTickets.central("!!IT WILL BE FOR THE NEXT ONE!!")
                    PrintTickets.horizontal_under()
                    PrintTickets.central("The ticket isn't winning...")
                    PrintTickets.horizontal_under()
                    pass

    # This method asks how much to bet                      
    def play_user(self):
        PrintTickets.horizontal_line()
        PrintTickets.central("Enter an amount between 1€ and 200€")
        PrintTickets.horizontal_under()
        # Loop which also handles errors
        while True:
            played = input("How much do you want to play on the ticket?: ")
            if played.isdigit():
                play_float = float(played)
                if play_float >= 1 and play_float <= 200:
                    self.play = play_float
                    break
                else: 
                    print("!!Enter an amount between 1€ and 200€!!")
                    print("Please, try again...")
                    print()
            
            else:
                print("!!Enter a numeric value!!")
                print("Please, try again...")
                print()
   
if __name__ == '__main__':
    ex = Lotto()
    ex.print_ticket(ex,3)