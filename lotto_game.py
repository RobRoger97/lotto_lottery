# Import methods from other files
from lotto.bills import Lotto
from argparse import ArgumentParser
from lotto.prints import PrintTickets

def main():
  arg_par = ArgumentParser(description="Lotto ticket generator")
  arg_par.add_argument("n", type = int, help="Number of ticket to generate", choices = [0, 1, 2, 3, 4, 5])
  args = arg_par.parse_args()
  # Associates the entered number by cmn line to tickets_num
  tickets_num = args.n

  while True:
    tickets_list = []
    # Case where zero entered --> exit
    if tickets_num == 0:
        PrintTickets.horizontal_line()
        print("       !!ATTENTION ENTERED 0!!\n      Thanks for participating,\n          see you next time!")
        PrintTickets.horizontal_under()
        print()
        print("Quitting...")
        break
    # If the number entered is in the desired range
    elif tickets_num>=1 and tickets_num<=5:
        ticket = Lotto()
        ticket.ticket_amount = tickets_num
        ticket.print_ticket(ticket,args.n)

        print()
        PrintTickets.horizontal_line()
        print("            !!ATTENTION!!\n       Do you want to continue?")
        PrintTickets.horizontal_under()
        print()
        tickets_num = int(input("- Yes ---> Enter a number between 1 and 5: \n" \
                                "-  No ---> Enter 0 to quit: \n"\
                                "\nEnter here: "))
    # # If the number entered is out of range
    else:
        PrintTickets.horizontal_line()
        print("            !!ATTENTION!!\n     That number is out of range!")
        PrintTickets.horizontal_under()
        print()
        print("Please, try again...")
        print()
        tickets_num = int(input("- Yes ---> Enter a number between 1 and 5 \n" \
                   "-  No ---> Enter 0 to quit: \n"\
                   "Enter here: "))


    

if __name__ == '__main__':
    main()