import random

random_num = random.randint(0,100)

number_guesses = 1

while True:
    guess = int(input("guess a random number \n"))

    if guess < random_num:
        number_guesses += 1
        print("the number you want is higher")
    elif guess > random_num:
        number_guesses += 1
        print("the number you want is lower")
    else:
        print("you got it right!!!")
        if number_guesses == 1:
            print("it took you", number_guesses, "guess, noice")
        else:
            print ("it took you", number_guesses, "guesses")
        break
