class City(object):
    """
        Represent the city (aka 'ruota') of bill
        (for the project purpose completely ignore 
         "ruota nazionale" and the "estratto determinato" play type)
        Attributes are:
        - city that belongs to the following list:
          (Bari, Cagliari, Firenze, Genova, Milano, 
           Napoli, Palermo, Roma, Torino, Venezia and Tutte)
    """    
    # List containing all cities
    cities_list = ["Bari", "Cagliari", "Firenze", "Genova", "Milano",
                   "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte" ]

    def __init__(self,city):
        # Don't distinguish between uppercase or lowercase letters
        # Don't consider the side characters to the string of interest
        city = city.strip().lower()
        # Capitalizes the first letter
        city = city.capitalize()
        if City.is_city_valid(city):
            self.city = city
        else:
            pass

    @staticmethod
     # Check if the bill type is contained in the list
    # Return True: if the city is in cities_list 
    # Else return False.
    def is_city_valid(city):
        # Don't distinguish between uppercase or lowercase letters
        # Don't consider the side characters to the string of interest
        city = city.strip().lower()
        # Capitalizes the first letter
        city = city.capitalize()

        if city in City.cities_list:
            return True
        else:
            print()
            print("         !!ATTENTION!!")
            print("The city entered is not VALID!")
            print()
            return False

# Example to confirm what was written
if __name__ == '__main__':
    example = City("       nAPOLI       ")
    print()
    print(f"This is:    {example.city}")
    print()
    print("If I try to enter 'Hello' the result is:")
    print()
    example = City("     Hello     ")