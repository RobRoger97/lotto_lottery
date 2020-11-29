# Learning path:
## Level 3 : _Lotto calculate prizes_
### Introduction
In the third level, the user is asked for a price to bet (ranging from 1€ to 200€).  
If the ticket is successful, based on a certain combination, number and bet, the price will be calculated with a certain algorithm. If the winnings exceed 500€, a certain tax (8%) will be calculated to be subtracted.  
The maximum payout for a ticket is 6,000,000€.
For more info on the rules visit: 
- https://www.sisal.it/lotto/come-si-gioca ;
- https://www.estrazionedellotto.it/prontuario-vincite-lotto .


#### Example of table's design:
The extraction's table shows the current date and 5 random numbers for each city.
```
+------------------------------------+
|         *_-_L O T T O_-_*          |
+====================================+
|           EXTRACTION OF:           |
|             27/11/2020             |
+====================================+
   Bari             51 03 75 89 86
   Cagliari         37 72 31 18 23
   Firenze          66 13 26 79 80
   Genova           81 06 87 33 32
   Milano           57 03 67 65 46
   Napoli           01 40 23 75 85
   Palermo          57 55 21 52 54
   Roma             02 30 45 64 82
   Torino           84 03 61 47 15
   Venezia          12 80 48 14 28
+------------------------------------+
```


#### Example of winner ticket's design: 
An example of a ticket will be presented below showing:   
_Tutte_ (all cities), _ambata_ (bet) and a random number.

```
+------------------------------------+
|        *_-_LOTTO TICKET_-_*        |
+====================================+
|                                    |
|            CITY: Tutte             |
|            BET: ambata             |
|           AMOUNT: 200.0€           |
|                                    |
+====================================+
|                 75                 |
|                                    |
+------------------------------------+
```
In the city _Bari_ there is the number 75 so ...
```
+------------------------------------+
|    !!YOUR TICKET IS A WINNER!!     |
+====================================+
|            RUOTA Tutte             |
|    With ambata on the numbers:     |
|                 75                 |
+====================================+
```
Since the payout is over 500€, applying the 8% tax, the net payout will be ...
```
+------------------------------------+
|        GROSS WIN: 2246.00€         |
|          NET WIN: 206.63€          |
+====================================+
```  

### How to launch the program
The entry point lotto_game.py script can be launched through command line by specifying the amount of tickets to generate for the n argument.  
For example, writing ***lotto_game.py 5*** will generate a bill of _five_ tickets.  
After launching the script, the program will start constructing each ticket by asking the user all the information about each ticket.

### Structure
The project is structured in a ***lotto_game.py*** file accompanied by a lotto package.
#### lotto package:
It is characterized by the presence of files such as:
- ***type_of_bill.py*** : it represents the chosen bet for a specific ticket;
- ***city.py*** : it represents the chosen city for a specific ticket;
- ***prints.py*** : it prints the ticket taking into account the locations of cities, bets and numbers;
- ***bills.py*** : it manages the logic of the program. It contains the lot class which takes into account the inputs and then enriches the ticket through the print file;
- ***extraction.py*** : it manages the 5 random numbers to be assigned to the cities and then prints the table of extractions, also considers the winning tickets;
- ***prizes.py*** : it takes care of checking the total premium based on the data entered by the user.