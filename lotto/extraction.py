from random import randrange
from time import strftime
# Call the classes from the files
from lotto.city import City
from lotto.prints import PrintTickets

# Go to specify the printing of the lottery 
# drawings of 5 numbers for each city
class PrintExtraction(object):
    """
        Represents the layout of the extraction table.
    """
    @staticmethod
    def extraction_table(extraction):
        txt = "*_-_L O T T O_-_*"
        # Current date of the draw
        current_date = strftime("%d/%m/%Y")
        PrintTickets.horizontal_line()
        PrintTickets.central(txt)
        PrintTickets.horizontal_under()
        PrintTickets.central("EXTRACTION OF:")
        PrintTickets.central(current_date)
        PrintTickets.horizontal_under()
        # Loop that describes the assignment of the 5 numbers 
        # to the single cities
        for name_city,num_rand in extraction.items():
            number = ["%02d" % x for x in num_rand]
            print("  ", name_city," "*(15-len(name_city))," ".join(number))

        PrintTickets.horizontal_line()

class Extraction(object):
    """
        Represents the extraction of the lottery.
    """
    def __init__(self):
        cities_numbers = {}
        for name_city in City.cities_list[:-1]:
            cities_numbers[name_city] = Extraction.random_numbers()
        self.cities_numbers = cities_numbers
    # Method that prints the table containing the results of the extraction
    def print_extraction(self):
        PrintExtraction.extraction_table(self.cities_numbers)
    # Method that displays if the ticket is winning
    def is_winner(self, city, numbers):
        win_num = []
        for key,value in self.cities_numbers.items():
            if city == key:
                for n in numbers:
                    if n in value:
                        win_num.append(n)
                return win_num
            # Special case in which the user enters "Tutte"
            elif city == "Tutte":
                for n in numbers:
                    if n in value:
                        win_num.append(n)
                return win_num
            else:
                pass
            
    # Method that calculates the 5 random numbers            
    @staticmethod
    def random_numbers():
        num_list = []
        for n in range(5):
            num = randrange(1,90+1)

            while True:
                if num in num_list: # If the number exists, repeat..
                    num = randrange(1,90+1)
                else:
                    break
            num_list.append(num)
        return num_list

if __name__ == '__main__':
    test = Extraction()
    test.print_extraction()
    lis = [1,2,3,5,7,10,4,6,12,24]
    test.is_winner('Tutte',lis,'ambata',1)
