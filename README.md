# Learning path:
## Level 1 : _Lotto Ticket Generator_
### Introduction
In this first level, 1 to 5 tickets will be generated.  
If _zero_ is entered, the output will be forced.  
In order to do this, the user will be required:
- the city of extraction _(napoli, firenze, bari, cagliari, venezia, milano, roma, genova, palermo o torino)_;
- the type of bet _(ambata, ambo, terno, quaterna or cinquina)_;
- the amount of numbers to be placed (between 1 and 10), then the program will generate sequences of random numbers between 1 and 90. The choice of numbers must be consistent with the bet chosen.
For example, if the user bets ***terno***, he cannot choose less than 3 numbers.

#### Example of a visual representation:
An example of a ticket will be presented below showing:   
_Napoli_ (city), _terno_ (bet) and four random numbers.

>+------------------------------------+  
>|        *_-_LOTTO TICKET_-_*        |  
>+====================================+  
>|                                    |  
>|            CITY: Napoli            |  
>|                                    |  
>|             BET: terno             |  
>|                                    |  
>+====================================+  
>|            34 25 59 13             |  
>|                                    |  
>+------------------------------------+  

### How to launch the program
The entry point lotto_game.py script can be launched through command line by specifying the amount of tickets to generate for the n argument.  
For example, writing ***lotto_game.py 5*** will generate a bill of _five_ tickets.  
After launching the script, the program will start constructing each ticket by asking the user all the information about each ticket.

### Structure
The project is structured in a ***lotto_game.py*** file accompanied by a lotto package.
#### lotto package:
It is characterized by the presence of files such as:
- ***type_of_bill*** : it represents the chosen bet for a specific ticket;
- ***city*** : it represents the chosen city for a specific ticket;
- ***prints*** : it prints the ticket taking into account the locations of cities, bets and numbers;
- ***bills*** : it manages the logic of the program. It contains the lot class which takes into account the inputs and then enriches the ticket through the print file