class Prize(object):
    """
        Represents the prices for each bet associated with the numbers played
        Attributes:
        - win_combination : how many combinations from 1 to 10 numbers you can 
                            play on a single Lotto game ticket
        - amount : gross amount of Lotto winnings obtained by wagering € 1 on a 
                   single wheel, playing from 1 to 10 numbers with the various 
                   game options.
    """
    # The following dictionary shows which and how many combinations from 1 to 10 numbers 
    # can be played on a single Lotto game card. 
    # Keys are numbers, values ​​are combinations.
    win_combination = { 1: [1],
                        2: [2, 1],
                        3: [3, 3, 1],
                        4: [4, 6, 4, 1],
                        5: [5, 10, 10, 5, 1],
                        6: [6, 15, 20, 15, 6],
                        7: [7, 21, 35, 35, 21],
                        8: [8, 28, 56, 70, 56],
                        9: [9, 36, 84, 126, 126],
                       10: [10, 45, 120, 210, 252]}

    # The following dictionary shows the gross Lotto winnings obtained by wagering € 1 on 
    # a single wheel, playing 1 to 10 numbers with the various game options.
    # Keys are numbers, values are the gross Lotto winnings.
    gross_winnings = { 1: [11.23],
                       2: [5.61, 250],
                       3: [3.74, 83.33, 4500],
                       4: [2.80, 41.66, 1125, 120000],
                       5: [2.24, 25, 450, 24000, 6000000],
                       6: [1.87, 16.66, 225, 8000, 1000000],
                       7: [1.60, 11.90, 128.57, 3428.57, 285714.28],
                       8: [1.40, 8.92, 80.35, 1714.28, 107142.85],
                       9: [1.24, 6.94, 53.57, 952.38, 47619.04],
                      10: [1.12, 5.55, 37.50, 571.42, 23809.52]}



    def __init__(self, win_combination = 0, amount = 0.00):
        self.win_combination = win_combination
        self.amount = amount

    # Extract from the dictionary the combination appropriate to the numbers and value of the bet
    def calculate_comb (self, bet_int, num):
        for key,value in Prize.win_combination.items():
            if len(num) == key:
                self.win_combination = value[bet_int - 1]
                return self.win_combination
                
    # Extract from the dictionary the amount appropriate to the numbers and value of the bet
    def calculate_amount(self, bet_int, num):
        for key,value in Prize.gross_winnings.items():
            if len(num) == key:
                self.amount = value[bet_int - 1]
                return self.amount

        