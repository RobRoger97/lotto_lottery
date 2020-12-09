from random import sample
from time import strftime
# Call the classes from the files
from lotto.city import City
from lotto.print import Print

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
        Print.horizontal_line()
        Print.central(txt)
        Print.horizontal_2line()
        Print.central("EXTRACTION OF:")
        Print.central(current_date)
        Print.horizontal_2line()
        # Loop that describes the assignment of the 5 numbers 
        # to the single cities
        for name_city,num_rand in extraction.items():
            number = ["%02d" % x for x in num_rand]
            print("  "*3, name_city," "*(20-len(name_city))," ".join(number))

        Print.horizontal_line()

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
        next_step = Print.next_step(Print)
        PrintExtraction.extraction_table(self.cities_numbers)
            
    # Method that calculates the 5 random numbers            
    @staticmethod
    def random_numbers():
        return sample(list(range(1,90+1)),5)

if __name__ == '__main__':
    test = Extraction()
    test.print_extraction()