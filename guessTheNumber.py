import random
while True:
	n = random.randint(0,100)
	count = 0
	while True:
		guess = int(input('Guess a number between 1 and 100:'))
		if guess == n:
			print("You win")
			count += 1
			print("You tried "+str(count)+" times.")
			play_again = input('Do you want to play again?')
			if play_again == 'no':
				print('Bye')
				quit()
			else:
				break
		elif guess > n:
			print('Try a smaller number')
			count += 1 
		elif guess < n:
			print('Try a larger number')
			count += 1