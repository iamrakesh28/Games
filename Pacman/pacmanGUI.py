import pacmanBFS
import escape
import pygame


block_size = 50
class Game :
	def __init__(self, time, filename = 'pacmanMatrix'):
		fp = open(filename,'r')
		data = fp.readlines()
		self.matrix = []
		self.row = len(data)
		self.col = None
		self.score = 0
		self.ghost = ()
		self.time = time
		self.over = False
		self.win = False
		self.pac = ()
		self.fruit = ()
		i = 0
		for line in data:
			self.col = len(line) - 1
			self.matrix.append([])
			j = 0
			for j in range(len(line) - 1):
				self.matrix[i].append(' ')
				if line[j] == 'p':
					self.pac = (i,j)
				elif line[j] == 'g':
					self.ghost += ((i,j),)
				elif line[j] == '#':
					self.matrix[i][j] = '#'
				elif line[j] == 'f':
					self.matrix[i][j] = 'f'
					self.fruit += ((i,j),)
			i += 1

	def display(self):
		s = ''
		for i in range(self.row):
			for j in range(self.col):
				s += self.matrix[i][j]
			s += '\n'
		print(s)

	def valid(self, i, j):
		if i >= 0 and i < self.row and j >= 0 and j < self.col:
			if self.matrix[i][j] != '#':
				return True
			return False
		return False

	def eat(self):
		fruit = ()
		ghost = ()
		win = False
		game_over = False
		for i,j in self.fruit:
			if (i,j) == self.pac:
				self.time = 40
			else:
				fruit += ((i,j),)
		self.fruit = fruit

		for i,j in self.ghost:
			if (i,j) == self.pac:
				if self.time == 0:
					win = False
					game_over = True
					ghost += ((i,j),)
			else:
				ghost += ((i,j),)
		self.ghost = ghost

		if len(self.ghost) == 0:
			win = True
			game_over = True
		self.over = game_over
		self.win = win

	def lose(self):
		if self.win == True : 
			print('You Won')
			print('Your time = ', self.score)
		else:
			print('Game Over')

class window:
	def __init__(self, row, col):
		pygame.init()
		self.background = (33, 33, 33)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((col * block_size, row * block_size))
		pygame.display.set_caption('Pacman')
		self.store = {}

		# Left Pacman
		image = pygame.image.load('pac.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_left1'] = image
		image = pygame.image.load('pac1.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_left2'] = image

		# Right Pacman
		image = pygame.image.load('pac_right.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_right1'] = image
		image = pygame.image.load('pac1_right.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_right2'] = image
		
		# Fruit
		image = pygame.image.load('fruit.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['fruit'] = image

		# Obstacle
		image = pygame.image.load('block.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['block'] = image
		
		# Ghost
		image = pygame.image.load('red_ghost.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['red_ghost'] = image
		image = pygame.image.load('cold_ghost.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['cold_ghost'] = image

	def display(self, matrix, time, direct, even, pac, ghost):
		self.screen.fill(self.background)
		row = len(matrix)
		col = len(matrix[0])
		for i in range(row):
			for j in range(col):
				if matrix[i][j] == ' ':
					continue
				if matrix[i][j] == '#':
					self.screen.blit(self.store['block'], (block_size * j, block_size * i))
				else :
					self.screen.blit(self.store['fruit'], (block_size * j, block_size * i))
		
		# Ghost and Pacman
		coord = (block_size * pac[1], block_size * pac[0])
		if direct == 0:
			if even:
				self.screen.blit(self.store['pac_left1'], coord)
			else:
				self.screen.blit(self.store['pac_left2'], coord)
		else:
			if even:
				self.screen.blit(self.store['pac_right1'], coord)
			else:
				self.screen.blit(self.store['pac_right2'], coord)
		for i, j in ghost:
			coord = (block_size * j, block_size * i)
			if time:
				self.screen.blit(self.store['cold_ghost'], coord)
			else:
				self.screen.blit(self.store['red_ghost'], coord)

'''
	move = 0 -> up
	move = 1 -> down
	move = 2 -> left
	move = 3 -> right

'''
def main() :

	G = Game(40)
	Win = window(G.row, G.col)
	game = True
	direct = 0
	move = -1
	delay = 2
	r, c = G.pac
	even = 0
	while game:
		#Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game = False
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP] and G.valid(G.pac[0] - 1, G.pac[1]): 
			move = 0
		elif pressed[pygame.K_DOWN] and G.valid(G.pac[0] + 1, G.pac[1]): 
			move = 1
		elif pressed[pygame.K_LEFT] and G.valid(G.pac[0], G.pac[1] - 1): 
			move = 2
			direct = 0
		elif pressed[pygame.K_RIGHT] and G.valid(G.pac[0], G.pac[1] + 1):
			move = 3
			direct = 1
 
		if move == 0 and G.valid(G.pac[0] - 1, G.pac[1]):
			r = max(r - 1, 1)
		elif move == 1 and G.valid(G.pac[0] + 1,G.pac[1]):
			r = min(r + 1, G.row - 2)
		elif move == 2 and G.valid(G.pac[0], G.pac[1] - 1):
			c = max(c - 1, 1)
		elif move == 3 and G.valid(G.pac[0], G.pac[1] + 1):
			c = min(c + 1,G.col - 2)

		G.matrix[G.pac[0]][G.pac[1]] = ' '
		for i,j in G.ghost:
			G.matrix[i][j] = ' '
		G.pac = (r, c)
		G.eat()
		if G.over == True:
			Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost)
			break
		
		if delay % 2:
			if G.time:
				G.ghost = escape.esc(G.matrix, G.pac, G.row, G.col, G.ghost)
			else:
				G.ghost = pacmanBFS.BFS(G.matrix, G.ghost, G.row, G.col, G.pac)
		
		delay = (delay + 1) % 2
		even = (even + 1) % 2
		Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost)
		G.eat()
		if G.over == True:
			Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost)
			break
		G.score += 1
		G.time = max(0,G.time - 1)
		Win.clock.tick(6)
		pygame.display.flip()
	

if __name__ == '__main__':
	main()
