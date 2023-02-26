from random import randint

random_range = (0, 100)
random_integer = randint(*random_range)
print(random_integer)


def input_int_check(user_input, int_range):
    try:
        user_input = int(user_input)

        if user_input <= int_range[1] and user_input >= int_range[0]:
            return user_input

        else:
            return None

    except:
        return None


def comparator(user_value, base_value, int_range):
    if user_guess == random_integer:
        print("Same integer.")
        quit()

    elif abs(user_value - base_value) >= (int_range[1] - int_range[0]) / 4:
        print("Way too {}!".format(("low", "high")[user_value > base_value]))

    else:
        print("Too {}!".format(("low", "high")[user_value > base_value]))


while True:

    user_guess = input_int_check(input("Guess?\n"), (0, 100))

    if user_guess:
        comparator(user_guess, random_integer, random_range)

    else:
        print("Numbers only!")
