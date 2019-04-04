# Using Artificial Intelligence algorithms to solve puzzles and play games:

## 1.  Move the Block : 

######	It is a puzzle game, where the player has to move the red block to blue position(exit). Green blocks are obstacles which may have to be moved to make room for the red block. Here, I have build two versions of it.

###	a. Game has only 1x1 square blocks (Games/Block/)
######	The game uses BFS algorithm to solve the puzzle in minimum steps. Each state is a configuration of the board.
#####	In terminal, use `python block.py` to run it.
	visual.py is used for visualiztion in Linux shell.
#	![Block Game](https://github.com/iamrakesh28/Games/blob/master/images/block.png)
	
###	b. Game has only 2x1 and 1x2 blocks (Games/BlockRect/)
######	The game uses BFS algorithm to solve the puzzle in minimum steps. Each state is a configuration of the board.
#####	In terminal, use `python blockRect.py` to run it.
	visual.py is a visualization file
#	![BlockRect Game](https://github.com/iamrakesh28/Games/blob/master/images/blockRect.png)

## 2.  Pacman (Games/Pacman/):
######	It is a classic game. Here, Ghosts use BFS algorithm to eat Pacman. When Pacman eats a fruit, ghosts runs in a 	direction  that maximizes its euclidean distance from the pacman (manhatten distance would be better).
#####	In terminal, use `python3 pacman.py` to run it.
	pacmanBFS.py gives shortest path from ghosts to pacman.
	escape.py gives the next position of ghosts to maximaize its distance from pacman
	visualPac.py is for viusalization
	pacmanMatrix is the input board configuration
#	![Pacman1](https://github.com/iamrakesh28/Games/blob/master/images/pacman1.png) 		![Pacman2](https://github.com/iamrakesh28/Games/blob/master/images/pacman2.png)

## 3. GridWorld (Games/QLearning):
######	It is just implementation of Q-Learning to solve GridWorld Problem.
## 4. Q-Learning on Pacman (Games/TrainPacman):
######	Here, I have used q-learning to play above pacman game. The board of the game is reduced to 7x9, such that the total possible states is about 10^6.
	train.py caluates the optimal decision.
	In terminal, use `python3 trainPacman.py` to run it.
	Each time the file is run, the game is trained.
#	![Pacman training](https://github.com/iamrakesh28/Games/blob/master/images/trainPacman.png)
