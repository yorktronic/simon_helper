# Script to help me beat the simon game

keys = []
colors = {1: 'Blue', 2: 'Green', 3: 'Yellow', 4: 'Red'}
user = ""
idx = 0


print ("Welcome to the Simon helper. If you have trouble remembering after 15" +
			" or so steps in the game Simon, then this will be of use to you \n")
print ("At the start of your Simon game, enter 1, 2, 3, or 4 at the promt for the" +
			" solver to store the color sequence. \n Blue = 1 \n Green = 2 \n Yellow = 3 \n" +
			" Red = 4 \n")

print ("Input 'r' at the prompt to return to the beginning and then press <ENTER> " +
			"and the helper will tell you the sequence, step by step. Input 'q' to quit.\n")

print ("Input 'a' at the prompt and the helper will print out the entire sequence.")



while user != ("q" or "Q"):
	
	user = raw_input(': ') #the prompt

	# Reset the start of the sequence to the beginning, for the user to replay it 
	if user == "r":
		idx = 0

	# Store the user input 
	elif user in ["1", "2", "3", "4"]:
		keys.append(int(user))

	# Print out the current step, if the user is walking back through the steps
	elif user is "":
		if idx < len(keys):
			print colors[keys[idx]]
			idx += 1
		else:
			print 'End of sequence.'

	# Print out the entire sequence up to the most recent step
	elif user == "a":
		for idy, key in enumerate(keys):
			print "Step {}: {}".format(idy+1, colors[key])



