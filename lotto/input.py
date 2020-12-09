from random import sample
# Import methods from other files
from lotto.city import City
from lotto.bet import TypeBill
from lotto.print_tickets import PrintTickets
from lotto.print import Print

class Input(object):
    """
        Represents the game inputs
    """
    def __init__(self, city ='', bet ='',num =[]):
        self.city = city
        self.bet = bet
        self.num = num
        self.int_bet = 0

    # Method in which the user is asked to enter the number 
    # of random numbers to play
    @staticmethod
    def number_user(self):
        max_num = 10 # Maximum number to respect

        while True:  
            print()          
            amount = input("How many numbers? \n"\
                           f"Enter a number from {self.int_bet} to 10\n"\
                           "---> ")
            print()
            # Case in which the user does not enter a number           
            if amount.isdigit()== False:
                Print.horizontal_2line()
                Print.central("This is not a number!")
                Print.central("Please, try again...")
                Print.horizontal_2line()
            else:
                if int(amount) >= self.int_bet and int(amount) <= max_num:
                    self.num = Input.random_numbers(int(amount))
                    break
                # If it is a number, we have to handle the errors 
                # in this case as well
                elif int(amount) < self.int_bet: # The type of bill must also be considered
                    Print.horizontal_2line()
                    Print.central("The number entered is too low")
                    Print.central("Please, try again...")
                    Print.horizontal_2line()

                elif int(amount) > 10:
                    Print.horizontal_2line()
                    Print.central("The number entered is out of range")
                    Print.central("Please, try again...")
                    Print.horizontal_2line()
                

    # Method in which the user is asked to enter the city
    @staticmethod
    def city_user(self):
        Print.horizontal_line()
        txt = "Choose one of the next cities"
        Print.central(txt)
        Print.horizontal_2line()
        # Creates a list of cities to observe from for the user can choose
        for x,name in enumerate(City.cities_list,1):
            print("%2.0f)"%(x), " ", name)
        
        Print.horizontal_line()

        while True:
            print()
            user_city = input("Enter the name of the city: ")
            print()
            # The method is called to verify that the city is valid
            if City.is_city_valid(user_city):
                c = City(user_city)
                self.city = c.city
                break
            elif user_city.isdigit(): # Case in which the user enter a number
                Print.horizontal_2line()
                Print.central("Enter the name of the city,")
                Print.central("not the number!")
                Print.central("Please, try again...")
                Print.horizontal_2line()

    # Method in which the user is asked to enter the type of bill
    @staticmethod            
    def type_user(self):
        Print.horizontal_line()
        txt = "Choose one of the next type of bill:"
        Print.central(txt)
        Print.horizontal_2line()
         # Creates a list of type to observe from for the user can choose
        for x,name in enumerate(TypeBill.types_list,0):
            if name!=None:
                print("%2.0f)"%(x), " ", name)
        Print.horizontal_line()

        while True:
            print()
            user_type = input("Enter the type of bill: ")
            print()
            # The method is called to verify that the type is valid
            if TypeBill.is_bill_valid(user_type): 
                b = TypeBill(user_type)
                self.int_bet = b.min_num
                self.bet = b.bill_type
                
                break
            elif user_type.isdigit(): # Case in which the user enter a number
                Print.horizontal_2line()
                Print.central("Enter the type of bill,")
                Print.central("not the number!")
                Print.central("Please, try again...")
                Print.horizontal_2line()

    # Method that takes the number entered by the user as an argument 
    # and creates lists of random numbers
    @staticmethod
    def random_numbers(number_amount):
        return sample(list(range(1, 90 + 1)), number_amount)