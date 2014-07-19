def welcome():
	print("Let's practice some python!")
	print("As Andrew would say, 'What would Python print...'")

def cs61a_quiz():

	welcome()
	questions=[["l=[1,2,3]", "l"], ["l=[1,2]", "l"], ["a=5", "a"], ["(lambda x:x*x)(2)"]]
	answers=["[1,2,3]","[1,2]", "5","4"]




	how_smart_you_are=1 #how difficult is the question / level
	correct_in_a_row=0
	how_fast_to_advance=0 #after this many correct answers in a row will advance to next level

	how_fast_to_advance=set_endurance()

	acceptable_answers={"y","yes", "yeah", "sure"}

	keepGoing="y"
	while keepGoing.lower() in acceptable_answers:
		clear_screen()


		print("level ",how_smart_you_are)
		print("correct answers in a raw: ", "* "*correct_in_a_row)

		display="the answer is : "

		prompt=">>>"
		welcome()
		for i in range(len(questions)):
			print("What would print?")
			for j in range(len(questions[i])):
				print(prompt+questions[i][j])
			answer=input(": ")
			if answer==answers[i]:
				print("Great!")
				correct_in_a_row+=1
				if correct_in_a_row==how_fast_to_advance:
					how_smart_you_are+=1
					correct_in_a_row=0
					congrat()
					print("You advanced to the next level!!!!")
			else:
				print("The correct answer is :", answers[i])
				how_smart_you_are-=1
				correct_in_a_row=0

	
		keepGoing=input("Let's do some more math(y = yes): ")

def clear_screen():
	print("\n"*40)

#I was really boared and tired :)
def congrat():
	print("   @@@@      @@       @@          @@       @@@@@      @@@@@@           @@@        @@@@@@@@@@@@    @")
	print("  @        @@  @@     @@ @@       @@     @@           @@    @@        @@  @@           @@         @")
	print(" @       @@      @@   @@  @@      @@   @@             @@    @@       @@    @@          @@         @")
	print("@       @@        @@  @@    @@    @@  @@              @@  @@        @@      @@         @@         @")
	print("@       @@        @@  @@     @@   @@  @@      @@@@@@  @@@          @@ @@@@@@ @@        @@         @")
	print(" @       @@      @@   @@      @@  @@   @@         @@  @@  @@      @@          @@       @@         @")
	print("  @        @@  @@     @@       @@ @@      @@    @@@   @@   @@    @@            @@      @@       ")
	print("   @@@@      @@       @@          @@        @@@@@     @@    @@  @@              @@     @@         @")

def info():
	print("This is a CS61A quiz program that will help you to master Python.")
	print("You can choose that how many questions you have to master in a row")
	print("to get to the next level.")
	
def set_endurance():
	"""This will allow the user to set that how many questions need to master
	before getting to the next level.
	"""
	endurance=int(input("Enter that how many questinos need to be answered correct in a row to advance to the next level:"))
	return endurance

cs61a_quiz()