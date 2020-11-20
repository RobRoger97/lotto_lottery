from random import randrange

from city import City
from type_of_bill import TypeBill
from prints import PrintTickets

class Lotto(object):

    """
        Represents a bill of the lotto game.
        Attributes are:
        - city (string)
        - bet  (string)
        - num  (list of random number)
        - ticket_amount (da vedere)
    """
    def __init__(self, city ='', bet ='',num =[], ticket_amount=0):
        self.city = city
        self.bet = bet
        self.num = num
        self.int_bet = 0
        
        if Lotto.is_ticket_amount_valid(ticket_amount):
            self.ticket_amount = ticket_amount
        else:
            pass
    

    @staticmethod
    def number_user(self):
        max_num = 10

        while True:            
            amount = input("How many numbers? \n \
                        Enter a number from 1 to 10\n \
                        ---> ")
            if amount.isdigit()== False:
                print("This is not a number!")
                print("Please, try again...")
                print()
            else:
                if int(amount) >= self.int_bet and int(amount) <= 10:
                    self.num = Lotto.random_numbers(int(amount))
                    break
                elif int(amount) < self.int_bet:
                    print("The number entered is too low")
                    print("Please, try again...")
                    print()

                elif int(amount) > 10:
                    print("The number entered is out of range")
                    print("Please, try again...")
                    print()
                


    @staticmethod
    def city_user(self):
        PrintTickets.horizontal_line()
        txt = "Choose one of the next cities"
        PrintTickets.central(txt)
        PrintTickets.horizontal_under()

        for x,name in enumerate(City.cities_list,1):
            print(" -%2.0f"%(x), "-->", name)
        
        PrintTickets.horizontal_line()

        while True:
            user_city = input("Enter the name of the city: ")

            if City.is_city_valid(user_city):
                c = City(user_city)
                self.city = c.city
                print(self.city)
                break
            elif user_city.isdigit():
                print("Enter the name of the city,\n "\
                    "not the number!")
                print("Please, try again...")
                print()
    @staticmethod            
    def type_user(self):
        PrintTickets.horizontal_line()
        txt = "Choose one of the next type of bill:"
        PrintTickets.central(txt)
        PrintTickets.horizontal_under()

        for x,name in enumerate(TypeBill.types_list,0):
            print(" -%2.0f"%(x), "-->", name)
        PrintTickets.horizontal_line()

        while True:
            user_type = input("Enter the type of bill: ")

            if TypeBill.is_bill_valid(user_type): 
                b = TypeBill(user_type)
                self.int_bet = b.min_num
                self.bet = b.bill_type
                print( self.int_bet, 'and', self.bet)
                break
            elif user_type.isdigit():
                print("Enter the type of bill,\n" \
                    "not the number!")
                print("Please, try again...")
                print()

    

    @staticmethod
    def random_numbers(number_amount):
        num_list = []
        for n in range(number_amount):
            num = randrange(1,90+1)

            while True:
                if num in num_list:
                    num = randrange(1,90+1)
                else:
                    break
            num_list.append(num)
        return num_list

    @staticmethod
    def is_ticket_amount_valid(ticket_amount):
        if ticket_amount >= 1 and ticket_amount <=5:
            return True
        else:
            return False
    @staticmethod
    def print_ticket(self,ticket_amount):
        dic = {'city' : [], 'bet' : [], 'num' : []}
        for t in range(ticket_amount):
            print()
            print(f"TICKET {t+1}:")
            print()
            Lotto.city_user(self)
            dic['city'].append(self.city)
            Lotto.type_user(self)
            dic['bet'].append(self.bet)
            Lotto.number_user(self)
            dic['num'].append(self.num)
        print(dic)
        for t in range(ticket_amount):    
            cit = dic['city']
            type_bill = dic['bet']
            num = dic['num']
            PrintTickets.table(cit[t],type_bill[t],num[t])


if __name__ == '__main__':
    ex = Lotto()
    ex.print_ticket(ex,3)