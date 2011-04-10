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
gamesWon = 0
gamesWonWithSwitch = 0
gamesLostWithSwitch = 0
gamesWonWithoutSwitch = 0
gamesLostWithoutSwitch = 0
doors = ['n','n','n']
doorToChoose = randint(0,2)
swap = randint(0,1)

for x in xrange(gameCount):
	shuffleDoors(doors)
	# Pick one door
	if doors[doorToChoose] == 'y':
		gamesWon += 1
	else:
		leftover = [0,1,2]
		leftover.remove(doorToChoose)
		newDoorToChoose = leftover[randint(0,1)]
		if (doorToChoose != newDoorToChoose) and doors[newDoorToChoose] == 'y':
			gamesWonWithSwitch += 1
		if (doorToChoose != newDoorToChoose) and doors[newDoorToChoose] == 'n':
			gamesLostWithSwitch += 1
		if (doorToChoose == newDoorToChoose) and doors[newDoorToChoose] == 'y':
			gamesWonWithoutSwitch += 1
		if (doorToChoose == newDoorToChoose) and doors[newDoorToChoose] == 'n':
			gamesLostWithoutSwitch += 1

print "\n\n"
print "Games won flatout: %d" % gamesWon
print "Games Won With Switch: %d" % gamesWonWithSwitch
print "Games Lost With Switch: %d" % gamesLostWithSwitch

print "\n\n"
print "=" * 3 + "Totals" + "=" * 3
print "Games Won: %d" % (gamesWon + gamesWonWithSwitch)
print "Games Lost: %d" % gamesLostWithSwitch
print "\n\n"
