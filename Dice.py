import random 
import time
end = 0
rolls = 0
roll_1 = 0
roll_2 = 0
roll_3 = 0
roll_4 = 0
roll_5 = 0
roll_6 = 0
while end != 1:
	roll = random.randint(1,6)
	time.sleep (2)
	throw = int(input("Type 1 to roll dice: "))
	if throw == 1:
		print ("Rolling dice...")
		time.sleep (2)
		print (roll)
		rolls += 1
		if roll == 1:
			roll_1 += 1 
		elif roll == 2:
			roll_2 += 1 
		elif roll == 3:
			roll_3 += 1
		elif roll == 4:
			roll_4 += 1 
		elif roll == 5:
			roll_5 += 1 
		else:
			roll_6 += 1
	else:
		end = 1
		print ("You've rolled", rolls, "times.\nYou've rolled 1", roll_1, "times\nYou've rolled 2", roll_2, "times\nYou've rolled 3", roll_3, "times\nYou've rolled 4", roll_4, "times\nYou've rolled 5", roll_5, "times\nYou've rolled 6", roll_6,"times" )
			
		
		
