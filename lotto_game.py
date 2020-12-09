# Import methods from other files
from lotto.lotto import Lotto
from argparse import ArgumentParser
from lotto.print import Print
from lotto.extraction import Extraction

def main():
    arg_par = ArgumentParser(description="Lotto ticket generator")
    arg_par.add_argument("n", type = int, help="Number of ticket to generate", choices = [0, 1, 2, 3, 4, 5])
    args = arg_par.parse_args()
  # Associates the entered number by cmn line to tickets_num
    tickets_num = args.n

    if tickets_num is None:
        Print.horizontal_line()
        Print.central("You can choice from 1 to 5 numbers of tickets")
        Print.central("or 0 to quit")
        Print.horizontal_2line()
        tickets_numb = int(input(" - How many tickets do you want to generate?: "))

    while True:
        try:
    # Case where zero entered --> exit
            if tickets_num == 0:
                Print.horizontal_line()
                Print.central("!!ATTENTION ENTERED 0!!")
                Print.central("Thanks for participating,")          
                Print.central("see you next time!")
                Print.horizontal_2line()
                print()
                print("Quitting...")
                break
    # If the number entered is in the desired range
            elif tickets_num>=1 and tickets_num<=5:
                lotto = Lotto()
                lotto.ticket_amount = tickets_num
                choices = lotto.generate_tickets(tickets_num)

                extraction = Extraction()
                extraction.print_extraction()

                lotto.lotto_tickets(lotto,choices,extraction)
                print()
                Print.horizontal_line()
                Print.central("!!ATTENTION!!")
                Print.central("Do you want to continue?")
                Print.horizontal_2line()
                print()
                tickets_num = int(input("- Yes ---> Enter a number of ticket (from 1 to 5): \n" \
                                        "-  No ---> Enter 0 to quit: \n"\
                                        "\nEnter here: "))
    # # If the number entered is out of range
            else:
                Print.horizontal_line()
                Print.central("!!ATTENTION!!")
                Print.central("That number is out of range!")
                Print.horizontal_2line()
                print()
                print("Please, try again...")
                print()
                tickets_num = int(input("- Yes ---> Enter a number of ticket (from 1 to 5): \n" \
                                        "-  No ---> Enter 0 to quit: \n"\
                                        "\nEnter here: "))
      # If a non-numeric value is entered                
        except ValueError: 
            Print.horizontal_line()
            Print.central("!!ATTENTION!!")
            Print.central("Enter a number!")
            Print.horizontal_2line()
            print()
            print("Please, try again...")
            print()
            tickets_num = int(input("- Yes ---> Enter of ticket (from 1 to 5): \n" \
                                    "-  No ---> Enter 0 to quit: \n"\
                                    "Enter here: "))

    

if __name__ == '__main__':
    main()