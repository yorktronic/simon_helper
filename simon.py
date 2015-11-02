########################################
#
# Script that helps a player beat the memory game Simon. Stores each step in the 
# game and allows the player to replay the steps, either step-by-step or by 
# printing all the steps.
#
########################################

# Stores each step, dictionary for numbers and colors, user input, and list index
keys = []
colors = {1: 'Blue', 2: 'Green', 3: 'Yellow', 4: 'Red'}
user = ""
idx = 0

# Function that prints the user input options in a table
def colprint(*args):
    for i in range(len(args)):
        print args[i] + "\t" ,

    print

# Function containing the instructions
def instructions():
	print ("Welcome to the Simon helper. If you have trouble remembering after 15" +
			" or so steps in the game Simon, then this will be of use to you \n")
	print ("At the start of your Simon game, enter 1, 2, 3, or 4 at the promt for the" +
			" solver to store the color sequence. See below for the color legend.\n")
	print ("User input options\n")

	colprint("1", "Blue")
	colprint("2", "Green")
	colprint("3", "Yellow")
	colprint ("4", "Red")
	colprint("r", "Replay sequence step-by-step (press ENTER) for each step")
	colprint("a", "Print all of the steps in the current game")
	colprint("c", "Clears the current game and restarts with a blank sequence")
	colprint("q", "Quit")

# Print the instructions for the user
instructions()

# The helper
while user != "q":
	
	# Prompt the user for input and make whatever the input is lowercase
	user = (raw_input(': ').lower())
	
	# Reset the list index to zero, so the user can replay each step 
	if user == "r":
		idx = 0

	# Store the user input if a valid number is provided
	elif user in ["1", "2", "3", "4"]:
		keys.append(int(user))

	# Print out the current step, if the user is walking through the steps
	elif user == "":
		if not keys:
			print "The sequence is empty"
		elif idx < len(keys):
			print colors[keys[idx]]
			idx += 1
		else:
			print 'End of sequence'

	# Print out the entire sequence up to the most recent step
	elif user == "a":
		if not keys:
			print "The sequence is empty"
		else:
			for idy, key in enumerate(keys):
				print "Step {}: {}".format(idy+1, colors[key])

	# Clears the sequence if the user wants to start a new game w/o restarting script
	elif user == "c":
		del keys[:]
		print "SEQUENCE CLEARED, STARTING NEW GAME \n"
		instructions()
