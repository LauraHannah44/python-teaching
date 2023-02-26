from random import randint

random_integer = randint(0, 100)

# while type(user_guess) != int:

while True:

    user_guess = input("Guess?\n")

    try:
        user_guess = int(user_guess)

        if user_guess == random_integer:
            print("Wow!")
            break

        else:
            print("Too {}!".format(("low", "high")[user_guess > random_integer]))

    except:
        print("Numbers only!")
