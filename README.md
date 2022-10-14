# RookPolynomials
Program generates a rook polynomial for given set of board.
Rook polynomial is a polynomial, where each factor desribes a number of posible settings of r rooks.
The task indicates that some fields may not be available to use.

![Zrzut ekranu 2022-10-14 105708](https://user-images.githubusercontent.com/47035195/195806677-89d7e43b-a715-4886-9ee2-00d61a9b26bc.png)

Instalation:

Program runs on pygame library. To instal this library go to comand line and use comand `py -m pip install -U pygame --user`. You may need to run as administrator.
If you're using OS other than Windows, visit this site: https://www.pygame.org/wiki/GettingStarted
When the instalation is ready, open file 'main.py' and run it.

![Zrzut ekranu 2022-10-14 105735](https://user-images.githubusercontent.com/47035195/195806702-b637b9f3-f3dc-4551-8fb4-c26591e6870a.png)

Features:

To disable a field, leftclick on it.
'Start' starts computing. 'Stop' stops it. After stoping, the computation will start all over again.
'Clear' set all fields to available.
'Reverse' set all avaible fields to disabled, and vice versa.
You can change a size of board form 1x1 to 9x9, but I recomend using this with caution. Computing full board 7x7 could take an hour. Consider making resonable limitations.

Coded by KarolWes, Feb 2021
