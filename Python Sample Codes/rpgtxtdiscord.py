print("Welcome adventurer! You have been chosen for a mighty quest due to your skill in magic and war!  Your mission will be to clear out the nearby cave and retrieve the Blade of Power from within.")

print()

print("INSTRUCTIONS: You will be presented with many Trials within the cave. When you need to make a choice, it will be presented in ALL CAPS.  Any other entry will cause the game to end, this includes hitting the spacebar.")

print()

print("Now, first things first. What is your weapon? ")

print()

weapon = input("My trusted: ")

print()

spell = input("A fine choice! Now choose a powerful battle spell!: ")

print()

print("Remember hero, magic requires energy so REST whenever you can! Your first trial awaits in yonder cave!  ")

print()

trial_1 = input("The cave's mouth opens before you wide and tall, yet you can tell there is light down in its gullet.  As you approach the sound of loose rocks awakens a single lone goblin sentry.  He is caught surprised by your arrival.  You may ATTACK or CAST").lower()

print()

if trial_1 == "attack":

    print("Your mighty " + weapon + " levels the cretin!")

elif trial_1 == "cast":

    print(spell + " lays the creature waste!")

else:
	
	print("Not a valid entry. Please try again")
	
	quit()

trial_2 = input("As the goblin falls, you continue down the cave to hear the squeaking chant of a feathered Goblin Shaman.  He locks eyes on you as you round the corner.  Choose to ATTACK or CAST Choose wisely.").lower()

print()

if trial_2 == "cast" and trial_1 == "attack":
    
    print("Your let " + spell + " fly from your lips before the stupid thing could think!  He slumps, defeated")

elif trial_2 == "cast" and trial_1 == "cast":
	
	print("Your magic fails you and the Shaman smiles as your own magic cooks you from the inside. Please try again")
	
	quit()
	
elif trial_2 == "attack":

    print("As you raise your " + weapon + " the Shaman screeches and roaring fireball burns you to a crisp.  You are dead.  Try again.")

    quit()
    
else:
	
	print("Not a valid entry. Please try again")
	
	quit()
	
print()

rest_1 = input("After the death of the Goblin Shaman, you spot an alcove with food and refreshment and even small bedding.  The way ahead seems clear and empty.  Do you WALK on or REST?").lower()

print()

if rest_1 == "walk":

    print("You continue on the path unhindered.  You go down further into the cave and with a sudden gust of cold, a Poltergeist moves through you from behind. The Ghost of a Kobold menaces you, pulling out a spectral sword to attack.")

elif rest_1 == "rest":

    print("You are well rested and fed.  You continue down further into the cave and with a sudden gust of cold, a Poltergeist moves through you from behind. The Ghost of a Kobold menaces you, pulling out a spectral sword to attack.")

else:
	
	print("Not a valid entry. Please try again")
	
	quit()
	
print()

trial_3 = input("Do you ATTACK or CAST?").lower()

print()

if trial_3 == "cast" and rest_1 == "rest":

    print("You take a second and " + spell + " blasts through the poltergeist!")

elif trial_3 == "attack":

    print("You immediately pull out " + weapon + " and it passes right through the spectral Kobold, who grins wickedly with it's spectral sword gleaming with an icy edge as it cuts your throat.  You are dead. Please try again")

    quit()

elif trial_3 == "cast" and rest_1 == "walk":

    print("You try to cast " + spell + " but it instead drains what little energy you have left and you black out.  The Kobold probably kills you.  Please try again.")

    quit()

else:
	
	print("Not a valid entry. Please try again")
	
	quit()
	
print()
    
trial_4 = input("As you stride past the formerly haunted corridor, the cave opens to a large cavern.  To your right is an Orc guard standing in front of a large wooden door. To your left is a darkened area with boxes and crates to cover behind.  Go right to ATTACK. Go left to SNEAK behind the boxes and crates").lower()

print()

if trial_4 == "attack":
	
	print("You rush the Orc, your " + weapon + " slicing through armor and bone")
	
elif trial_4 == "sneak":
	
	print("You creep through the darkness and find a safe spot to look out across the entire cavern.")
	
else:
	
	print("Not a valid entry. Please try again")
	
	quit()
	
if trial_4 == "attack":
	
	trial_4a = input("Killing the orc sentry has alerted his nearby friends.  You must now either face the coming reinforcements or go through the large wooden door, which is locked.  You can either ATTACK the coming horde or BASH through the door with your body").lower()

	if trial_4a == "attack":
		
		print("There are far too many for even you.  You are overwhelmed and killed.  Please try again")
		
		quit()
		
	if trial_4a == "bash":
		
		print("You bash through the wooden door, and turn to be met with three of the largest Daemons you have ever seen, the one in the middle is holding the Blade of Power in it's corrupted claws. As the sight startles you, the orc squad breaks through and takes you down from behind. Please try again.")
		
		quit()
		
if trial_4 == "sneak":
	
	trial_4b = input("From this side you can see the rest of the well-lit cavern.  You see the large garrison of Orcs commanding goblin grunts and one large commander further to your left.  He is yelling at a goblin, but then enters the command tent alone. But before you can decide what to do, you notice the crate next to you is open, packed with a single green potion. Do you DRINK the potion or STALK the Orc Commander?").lower()
	
print()
	
if trial_4b == "drink":
		
	print("You feel a mighty surge of power.  Your magic now has *unlimited* potential!  You skulk along the edge of the cavern to the back of the Commander's tent")
	
elif trial_4b == "stalk":
		
	print("You skulk along the edge of the cavern to the back of the Commander's tent.")
	
else:
		
	print("Not a valid entry. Please try again")
	
	quit()
	
print()
		
trial_5 = input("You stop at the edge of the tent and hear the orc Commander muttering to himself how those wretched Daemons are taking their sweet time planning locked behind that wooden door when they should be fighting, between big yawns and grunts. Finally you hear snoring drone through the tent. He is out cold. You pull the tent fabric up and pop in. In front of you is a massive Orc.  Do you KILL the Commander or just SWIPE the keys to the Daemons you must face down?").lower()

print()

if trial_5 == "swipe":
	
	print("After you take the keys, an Orc patrol walks by and hearing their snoring Commander, run in to wake him before the Daemons notice. Before you can think, the Commander hears the noise and stabs you from behind as the patrol lowers their weapons on you. You are dead. Because you let an Orc live. I hope you have learned your lesson. Try again.")
	
	quit()
	
elif trial_5 == "kill":
	
	print("You raise your " + weapon + " and execute the Orc Commander!  You take his keys and continue on your way towards the front of the tent.")

else:
	
	print("Not a valid entry. Please try again")
	
	quit()
	
print()
	
trial_6 = input("As you poke your head out of the tent, you see one guard outside at attention next to the tent in full plate armor, covering their entire body.  They even seem to be about your height.  Do you ATTACK, CAST or LURE them inside the tent?").lower()

print()

if trial_6 == "lure":
	
	print("With an authoritative bark you order the soldier to enter the tent and knock them unconscious with a hit on the head from behind.  They are out cold.  You remove the armor to reveal that one of your own kind is working with these foul creatures!  You place the armor upon yourself leaving them gagged and tied to a tent post.  You will deal with them later.")
	
elif trial_6 == "attack":
	
	print("You lunge at the foe with your faithful " + weapon +  " but alas they are as skilled in combat as you are!  After an extended time of exchanging blows, their reinforcements arrive and you are put down!")
	
	quit()
	
elif trial_6 == "cast" and trial_4b == "drink":
	
	print("You cast " + spell + ", but it is magnified beyond your own imagination.  " + spell + "-magic fills the cavern annihilating nearly every foe within.  There is nothing standing in your way but the lone Orc guarding the large wooden door, where according to the Orc Commander, the Daemons await.")
	
elif trial_6 == "cast":
	
	print("You cast " + spell + " at the foe with all your might but alas they are as skilled in magic as you are!  After an extended time of slinging exhausing spells, their reinforcements arrive and you are put down!")
	
	quit()
	
else:
	
	print("Not a valid entry. Please try again.")
	
	quit()
	
print()

if trial_6 == "cast" and trial_4b == "drink":
	
	trial_7a = input("From across the wreckage and carnage of the cavern, you stride towards the wooden door.  As you reach the half-way point you see the wooden door fly open as three Daemons walk out and gaze at the destruction.  Enraged, the Daemon holding the Blade of Power slays the last remaining Orc, and after searching for a few moments, locks eyes with you. This is it.  Will you ATTACK, CAST, or RUN?").lower()

	print()
	
	if trial_7a == "attack":
	
		print("You don't know how, but you are flying towards the Daemons with " + weapon + "in hand!  Daemonic limbs and gore drop to the floor in your fury.  After their bodies take such remarkable damage, they begin to burn away in Hellfire.  In the ashes, you see the Blade of Power gleam in the flames and pick it up.  It is then that you see your hands warped into claws, and feel the heavy leather wings flapping from your back...you are Daemonspawn now as you watch Hellfire light upon your arms and body.  The Daemons wanted the Blade of Power.  Now it is coming to them anyway.  The End.")
	
	quit()
	
	if trial_7a == "cast":
	
		print("You unleash a maelstrom of " +spell + ". It's magic rains from the ceiling. It erupts from the walls and the opens up from the floor. Daemonic bodies splattered with such power simply begin to fall apart.  After their bodies take such remarkable damage, they begin to burn away in Hellfire.  In the ashes, you see the Blade of Power gleam in the flames and pick it up.  It is then that you see your hands warped into claws, and feel the heavy leather wings flapping from your back...you are Daemonspawn now as you watch Hellfire light upon your arms and body.  The Daemons wanted the Blade of Power.  Now it is coming to them anyway. The End.")
	
		quit()
	
	elif trial_7a == "run":
	
		print("You turn to flee, only to be caught by large, swift-winged monstrosities well-accustomed to catching fleeing prey.  You are caught and brutally killed.")
	
		quit()
	
	else:
		print("Not a valid entry. Please try again.")
		quit()

print()

if trial_6 == "lure":
	
	trial_7b = input("Disguised in full plate armor you stride through the cavern and the ranks of Orcs, goblins, kobolds, and other evil creatures, monsters and beasts. You stand in front of the Orc standing guard and...he straightens up and stands aside. Strange...you pull out the key and enter.  Three Daemons stand and turn to you, and say Lord Betrayer! What is the meaning of this intrusion upon our machinations?  This is it. This is your one chance.  What do you do?  ATTACK, CAST or BLUFF").lower()
	
	print()
	
	if trial_7b == "cast" and trial_4b == "drink":
		
		print("With a thought, " + spell + " blasts through each Daemon, ripping them apart and leaving the room full of gore.  You stand in the midst unharmed.  You fall to the ground as the Potion and its effects wear off.  You then take the Blade of Power, and walk out, nodding to the Orc who resumes his post, and then out of the cave, and back to your home, where you are hailed as a hero!  Well done!  Victory is yours!")
		
	elif trial_7b == "bluff":
			
		print("You reply...There are many mysteries and powers the Blade of Power may possess that only my kind can extract from it, let me study it in to serve the cause...and they actually believe you!  With a grunt, the largest Daemon in the middle waves his hand and one of the others picks up the Blade of Power and hands it to you.  You then take the Blade of Power, and walk out, nodding to the Orc who resumes his post, and then out of the cave, and back to your home, where you are hailed as a hero!  Well done!  Victory is yours!")
		
else:
	
	print("The Daemons are not amused with your pathetic attempt at disturbing their council.  You are slaughtered for your insolence.")
	
	quit()
			