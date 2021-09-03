import random
#importing random to be able to generate random digits
guess=random.randint(1,99)
#the random digits generated should be between 1 and 99
while guess:
#the guessing should loop till a condition is met
    guess=random.randint(1,99)
#the random digits generated should be between 1 and 99
    jay=int(input("Guess a random number between 1 and 99: "))
#asking the user to input a random number
    if guess > jay:
        print("Sorry, your guess is too high.")
#print sorry your guess is too high when the guess is above the random digits
    elif guess < jay:
        print("Sorry, your guess is too low.")
#print sorry your guess is too low when the guess is above the random digits
    else:
        print("Congrats! you guessed right.")
        break
#break the loop