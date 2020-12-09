# Learning path:
## Level 2 : _Lotto Fake Extractions_
### Introduction
In the second level, a table of the numbers drawn for each city is generated. 
It is checked whether the ticket or tickets chosen are winning or not. 

#### When is the ticket winning?
The ticket results in ***winning*** when there is a least amount of matching numbers between the ticket's numbers and the numbers extracted in its city (for a bet on _Tutte_, namely all cities, the ticket's numbers will be checked against each city's extraction one by one). The least amount of matching numbers corresponds to the minumum amount of numbers to play for a specific bet type.

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
_Napoli_ (city), _ambata_ (bet) and a random number.

```
+------------------------------------+
|        *_-_LOTTO TICKET_-_*        |
+====================================+
|                                    |
|            CITY: Napoli            |
|                                    |
|            BET: ambata             |
|                                    |
+====================================+
|                 1                  |
|                                    |
+------------------------------------+
```  
In the city _Napoli_ there is the number 1 so ...
``` 
+------------------------------------+
|    !!YOUR TICKET IS A WINNER!!     |
+====================================+
|           RUOTA Napoli             |
|    With ambata on the numbers:     |
|                 1                  |
+====================================+
``` 

#### Example of loser ticket's design: 
An example of a ticket will be presented below showing:   
_Napoli_ (city), _ambata_ (bet) and a random number.

```
+------------------------------------+
|        *_-_LOTTO TICKET_-_*        |
+====================================+
|                                    |
|            CITY: Napoli            |
|                                    |
|            BET: ambata             |
|                                    |
+====================================+
|                10                  |
|                                    |
+------------------------------------+
``` 
In the city _Napoli_ there isn't the number 10 so ...
``` 
+------------------------------------+
|  !!IT WILL BE FOR THE NEXT ONE!!   |
+====================================+
|    The ticket isn't winning...     |
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
- ***bet.py*** : it contains the *"TypeBill"* class represents the chosen bet for a specific ticket;
- ***city.py*** : it contains the *"City"* class which represents the chosen city for a specific ticket;
- ***print.py*** : it manages screen printouts;
- ***ticket.py*** : it contains the *"Ticket"* class which is the ticket itself;
- ***print_tickets.py*** : it prints the ticket taking into account the locations of cities, bets and numbers;
- ***lotto.py*** : it manages the logic of the program. It contains the *"Lotto"* class which acts as a **"bridge"** between the various files created.
- ***extraction.py***: it manages the 5 random numbers to be assigned to the cities and then prints the table of extractions, also considers the winning tickets.