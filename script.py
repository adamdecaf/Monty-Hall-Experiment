# Monty Hall Experiment
# Adam Shannon
# 2011-04-09

from random import randint

def validateInt(message, error):
	while True:
		tmp = raw_input(message)
		try:
			return int(tmp)
		except:
			print error

def shuffleDoors(lyst):
	door = randint(0,2)
	for x in xrange(3):
		if x == door:
			lyst[x] = 'y'
		else:
			lyst[x] = 'n'
		
gameCount = validateInt("Enter the number of games: ", "Enter a number")
gamesWonWithSwitch = 0
gamesWonWithoutSwitch = 0
doors = ['n','n','n']

for x in xrange(gameCount):
	shuffleDoors(doors)
	# ...	
