import random
#importing random to be able to generate random digits
guess=random.randint(10,99)
#the random digits generated should be between 10 and 99
jay=random.randint(10,99)
#the random digits generated should be between 10 and 99
b=guess + jay
count = 1
while count <= 3:
    guess=random.randint(10,99)
#the random digits generated should be between 10 and 99
    jay=random.randint(10,99)
#the random digits generated should be between 10 and 99
    b=guess + jay
#declearing a variable b to add guess and jay
    x = print("What is", guess, "+", jay, "?")
#asking the user the question
    y = int(input("Answer "))
#asking the user for inputs
    if y == b:
        print("Correct!, you have gotten", count, "times")
        count +=1
    else:
        count = 1
        print("Incorrect, the expected number was", b)
print("Congrats, you've mastered addition")