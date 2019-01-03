import random
import sys

rand = random.randint(1,10)
print(rand)
guesses = []
tries = 0

while len(guesses) < 3:

	userNum = -1
	while ((userNum <= 0) or (userNum >=  11)):
		userNum = int( input("Enter in your guess (1-10): "))
		if (userNum <= 0) or (userNum >= 11):
			print("Guess is out of range between 1 to 10!")
	guesses.append(userNum)
	if (userNum == rand):
		print("That is the right number! You win!")
		print("Your guesses: ")
		print(guesses)
		sys.exit(0)
	else:
		print("Wrong number, try again! You have {} guesses left".format(2-tries))
		tries = tries + 1

print("I'm sorry, you did not guess the right number! You Lost.")
print("Your guesses: ")
print(guesses)

