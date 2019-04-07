#     Pacman Game
##### 1. pacmanMatrix
######  This is configuration file for Pacman Board. 'p' is for pacman, 'g' for ghost, 'f' for fruit and '#' for obstacle. If you want to change the board, make sure that after changes, total characters (including spaces) in each line is same and '#' should be on the border of the board. Put spaces for empty positions. 
##### 2. escape.py
######  This file gives next position of ghosts such that it maximizes the euclidean distance from the pacman.
##### 3. pacmanBFS.py
######  This file does Breadth First Search from pacman position and finds the shortest path to each ghosts. The ghosts uses this path to reach pacman in minimum time.

##### 5. visualPac.py
######  It takes board matrix, ghosts, fruits and pacman positions as input and displays in the shell.
##### 6. pacman.py
######  It is the main file. It takes board input from the pacmanMatrix.txt file. Displays the board using visualPac.py. Takes the input from the user. Gets the next position of ghosts from escape.py or pacmanBFS.py files.
##### To play the game, use `python3 pacman.py` in shell.
