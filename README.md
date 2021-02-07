# RookPolynomials
Program generates a rook polynomial for given set of board.
Rook polynomial is a polynomial, where each factor desribes a number of posible settings of r rooks.
The task indicates that some fields may not be available to use.

Instalation:

Program runs on pygame library. To instal this library go to comand line and use comand `py -m pip install -U pygame --user`. You may need to run as administrator.
If you're using OS other than Windows, visit this site: https://www.pygame.org/wiki/GettingStarted
When the instalation is ready, open file 'main.py' and run it.

Features:

To disable a field, leftclick on it.
'Start' starts computing. 'Stop' stops it. After stoping, the computation will start all over again.
'Clear' set all fields to available.
'Reverse' set all avaible fields to disabled, and vice versa.
You can change a size of board form 1x1 to 9x9, but I recomend using this with caution. Computing full board 7x7 could take an hour. Consider making resonable limitations.

What will be next
Generating each setings as a txt file

Coded by KarolWes, Feb 2021
