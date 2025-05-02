Connect4-Bots

The Connect4-Bot game is a well-known game where two players compete to be the first to align four tokens in a row—vertically, horizontally, or diagonally. 
This program features three game bots: one is good, while the other two are nearly perfect. 
The first bot operates based on the MinMax algorithm, the second also uses the MinMax algorithm but incorporates heuristics to make even better decisions. 
The third bot is built on the AlphaBeta algorithm, making it equally effective as the second bot, but significantly faster due to the enhanced MinMax algorithm.

How to Use:

In the avp.py file, you will find all the implemented bots. To choose a bot to play against, change agent = "      " to the name of your selected bot. 
By default, it is set to AlphaBetaAgent, and you can also specify whether you want it to be 'o' or 'x' (the 'o' player starts the game). Then, run this file and try to defeat the bot! :)

The ava.py file works similarly to avp.py, but here you will observe a game between two bots of your choice competing against each other. 
Just like in avp.py, you need to change agent1 = "    " and agent2 = "    " and specify which one will be 'o' and which one will be 'x'. Then, run this file.

I hope you have a lot of fun playing!😉
