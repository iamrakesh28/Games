#  Move the Block : 

######	It is a puzzle game, where the player has to move the red block to blue position(exit). Green blocks are obstacles which may have to be moved to make room for the red block. Here, I have build two versions of it.

###	  This Game has only 2x1 and 1x2 blocks
######	The game uses BFS algorithm to solve the puzzle in minimum steps. Each state is a configuration of the board. BFS starts on input state. On each state, it generates all next possible states and inserts in the queue. It only visits unvisited states (python dicitionary stores each state). When it reaches he goal states, the program prints the path and terminates.
#####	In terminal, use `python blockRect.py` to run it.
	    visual.py is a visualization file
#	![BlockRect Game](https://github.com/iamrakesh28/Games/blob/master/images/blockRect.png)

##### There is a tuple named 'obs' in line number 86 of blockRect.py file. Each element of the tuple is a tuple of pair. First element is the position of Red block and last element is the goal position (Blue). Rest all are obstacles. The first element (obs[i][0]) gives the position of one side of any block and second element (obs[i][1]) gives the ending position. (i,j) -> i*col + j, where i,j starts from 0.
##### To change the input configuration, change the values of the tuple 'obs'. For example, if you want to place the Red block first end in (2,2) and second end in (2,3), then set obs[0] = (2 * row + 2, 2 * row + 3)
