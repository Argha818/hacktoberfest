import random
import math
# Taking Inputs
a = int(input("Enter Lower bound:- "))

# Taking Inputs
b = int(input("Enter Upper bound:- "))


x = random.randint(a,b)
print("\n\tYou've only ",
     round(math.log(b - a + 2, 4)),
    " chances to guess the integer!\n")

# Initializing number of guesses.
c = 0


while c < math.log(b - a + 2, 4):
	c += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))


	if x == guess:
		print("Congratulations you did it in ",
			c, " try")
		
		break
	elif x > guess:
		print("The guessed number is too small!")
	elif x < guess:
		print("The number is too Guessed too high!")


if c >= math.log(b - a + 2, 4):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
