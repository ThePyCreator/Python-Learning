# These are my variables for the program
from datetime import datetime
sBotName = "SmartBot"
sYourName = "someone"
sTextInput = ""
now = datetime.now()


# this is a special object called a dictionary. Dictionaries in Python work kind of like a dictionary would in real life -
# if you want to find something, you lookup a word in the dictionary and find what it means, right? So, if you have an
# entry in the dictionary for a particular word, we'll call that the 'KEY' and the meaning of that word that you'll find in
# the dictionary is something we will call the VALUE. Sometimes, dictionaries are called key:value pairs too!
# we can add or remove words from the dictionary inside our program...
dictKnowledge = {"learn" : "That's a great idea, learning is always a good move!" }

# I'm going to do a little bit of introduction now'
print("Hello! My name is %s I am an AI made from Myles Nolan." % sBotName)

# Let's make sure they give us a name that isn't blank or just 'someone''
while sYourName == "someone" or sYourName == "":
	sYourName = input("Before you start, can you tell me your name, please? ")
	
# Now we'll start the discussion'
print("Ok, let's have some fun together. I'll ask you what you want and will keep playing until you type 'exit'.")

# until they enter the word exit, we'll keep going in this loop!'
# when we write ==, it means to check if something is equal, not the same as just =, that sets something to that value
# when we write !=, that means to check if something is NOT EQUAL. The exclamation (!) means NOT.
while sTextInput != "exit":
	print("(you can say solve for math equations, say name for your name, change name to change the bot name, bot name to see bot name, and to see time say time)")
	sTextInput = input("What would you like?: ").lower()
	
	if(dictKnowledge.get(sTextInput,False) != False):
		print("Oh, I know what to do with that input.\n%s" % dictKnowledge[sTextInput])
	elif( sTextInput == "what is your name" or sTextInput == "what's your name" or sTextInput == "whats your name" or sTextInput == "bot name"):
		print ("My name is %s" % sBotName)
	elif(sTextInput.find ("time")!=-1):
		print ("the current time is", now)

	elif(sTextInput.find("change") != -1 and sTextInput.find("name") != -1):		
		sBotNewName = ""
	
		while(sBotName == sBotNewName or sBotNewName == ""):
			sBotNewName = input("What would you like my name to be?")
	
		sBotName = sBotNewName
		print("Fine! My name is now %s." % sBotName)

	elif(sTextInput.find("solve")!=-1):
		sEquation = ""
		x = 0
		sAns = ""
		
		while(sEquation == ""):
				sEquation = input("Enter your math equation(*is multiply /is divide - is subtract + is add): ")
#/ is divide * is multiply - is subtract + is add				
		
		print("Ok, got your equation: %s." % sEquation)
		sAns = eval(sEquation)
		
		print("Ready for it? The answer to your math problem is %s." % sAns )
						
#.find is a function so if it finds that word or letter it does that input -1 means it did not find that word (reason tells bot name when says bot name instead of your name is because of the positioning [like the if statement above the your name statement])
	elif(sTextInput.find("name")!=-1):
		print ("your name is %s"% sYourName)
		
	elif (sTextInput != "exit"):
		sAction = ""
		
		print("Hmm, I'm not sure what to do when you want to %s." % sTextInput)
		
		while (sAction == ""):
			sAction = input("Can you tell me what I should do? ")
		
		dictKnowledge[sTextInput] = sAction

# all done, let's just be nice and say goodbye'
print("Goodbye! I'll miss you, %s." % sYourName.capitalize())
	
