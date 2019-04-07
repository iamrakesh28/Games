#     Q-Learning on Pacman Game
##### 1. pacmanMatrix
######  This is configuration file for Pacman Board. 'p' is for pacman, 'g' for ghost, 'f' for fruit and '#' for obstacle. If you want to change the board, make sure that after changes, total characters (including spaces) in each line is same and '#' should be on the border of the board. Put spaces for empty positions. 
##### 2. escape.py
######  This file gives next position of ghosts such that it maximizes the euclidean distance from the pacman.
##### 3. pacmanBFS.py
######  This file does Breadth First Search from pacman position and finds the shortest path to each ghosts. The ghosts uses this path to reach pacman in minimum time.
##### 4. train.py
######  Q-Learning is implemented in this file. It takes the following input:
    a. Current and previus positions of ghosts and pacman (previous position is used for calculating velocity)
    b. Number of fruits and change in fruit number
    c. Who is chasing whom
    d. Minimum distance of fruit and ghost from pacman
    e. The game is over or not. If over, then is it a lose or win
###### Reward function is based on these inputs.
###### All these data is stored as a state. States are stored in python dicitionary. 
##### 5. visualPac.py
######  It takes board matrix, ghosts, fruits and pacman positions as input and displays in the shell.
##### 6. trainPacman.py
######  It is the main file. It takes board input from the pacmanMatrix.txt file. Displays the board using visualPac.py. Takes the input from the user or bot about its action. Gets the next position of ghosts from escape.py or pacmanBFS.py files. Gives the required inputs to the train.py file. train.py takes the optimal action (when the bot is playing) and send it back to trainPacman.py. Each time the file is run, it takes the previously learned Q-values, actions, states, etc from Q, action, memo, state, etc. files. Each the game is played, it learns and stores in these files.

##### To run the game, use `python3 trainPacman.py` in shell.
