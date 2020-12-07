from lotto.print import Print

class TypeBill(object):
    """
        Represent the type of bill
        Attributes are:
        - bill_type that belongs to the following list:
          (ambata, ambo, terno, quaterna and cinquina)
        - the minimum number you can enter, based on the type
    """
    # List containing the various types of bill
    types_list = [None, 'ambata', 'ambo', 'terno', 'quaterna', 'cinquina']

    def __init__(self,bill_type):
        # Don't distinguish between uppercase or lowercase letters
        # Don't consider the side characters to the string of interest
        bill_type = bill_type.lower().strip()

        if TypeBill.is_bill_valid(bill_type):
            self.bill_type = bill_type
            self.min_num = TypeBill.types_list.index(bill_type)
        
        else:
            pass
      
    @staticmethod
    # Check if the bill type is contained in the list
    # Return True: if the bet_type is in types_list 
    # Else return False.
    def is_bill_valid(bill_type):
        # Don't distinguish between uppercase or lowercase letters
        # Don't consider the side characters to the string of interest
        bill_type = bill_type.lower().strip()

        if bill_type in TypeBill.types_list:
            return True
        
        else:
            Print.horizontal_2line()
            Print.central("!!ATTENTION!!")
            Print.central("The type entered is not VALID!")
            Print.horizontal_2line()
            return False

# Example to confirm what was written
if __name__ == '__main__':
    example = TypeBill("       AmbAtA       ")
    print()
    print(f"This is:    {example.bill_type}")
    print(f"The min numbers: {example.min_num}")
    print()
    print("If I try to enter 'Hello' the result is:")
    print()
    example = TypeBill("     Hello     ")