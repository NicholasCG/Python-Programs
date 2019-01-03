import random
import sys

rand = random.randint(1,10)

tries = 1
guesses = []

while(True):
	userNum = -1
	while ((userNum <= 0) or (userNum >=  11)):
                userNum = int( input("Enter in your guess (1-10): "))
                if (userNum <= 0) or (userNum >= 11):
                        print("Guess is out of range between 1 to 10!")

	guesses.append(userNum)

	if (userNum == rand):
		print("That is the right number! You win!")
		print("You guessed {} times!".format(tries))

		print("Your guesses: ")
		print(guesses)
		sys.exit()

	else:
		print("Wrong number, try again!")
		tries = tries + 1
		if (userNum > rand):
			print("Go lower!")
		else:
			print("Go higher!")
