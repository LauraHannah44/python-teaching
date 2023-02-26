from random import shuffle

num_of_apples = 3

desired_oranges = 2

anger_value = 0

base_retorts = ["What? I asked you how many oranges you got me.",
                "No no you weren't listening, I asked how MANY oranges you got me.",
                "...Is this some kind of a joke to you? Just tell me how many oranges you got me."]

random_retorts = ["I'm furious.",
                  "I can't believe this...",
                  "I'm nearly at the end of my tether.",
                  "I'd like you to stop.",
                  "I've had enough. Please just tell me.",
                  "I can't believe you think this is funny.",
                  "I only want a number. A simple number, please for the love of oranges.",
                  "..."]
shuffle(random_retorts)
retorts = base_retorts + random_retorts

#take user input
orange_input = input("How many oranges did you get me?\n")

#input test
while type(orange_input) == str:

    try:
        orange_input = int(orange_input)
    except:
        #not an integerable string

        if anger_value < len(retorts):
            string = retorts[anger_value] + "\n"

        else:
            print("I give up.")
            quit()

        anger_value += 1

        orange_input = input(string)

num_of_oranges = orange_input

print("apples: {}\noranges: {}".format(num_of_apples, num_of_oranges))

#test for correct number
if num_of_oranges == desired_oranges:
    print("Wow!")

elif num_of_oranges == 0:
    print("WHERE ARE THEY")

elif num_of_oranges < 0:
    print("Noooo, not my oranges!")

elif num_of_oranges < desired_oranges:
    print("Oh, you need to bring me {} more".format(desired_oranges - num_of_oranges))

elif num_of_oranges >= 4 * desired_oranges:
    print("What do you want, a medal?")

else:
    print("You've given me {} too many!".format(num_of_oranges - desired_oranges))


magnitude = int(num_of_oranges / abs(num_of_oranges))
for i in list(range(0, num_of_oranges, magnitude)):
    plural_or_not = ("s", "")[i == 0]
    comma_or_dot = (",", ".")[i == num_of_oranges - 1]
    print("{} orange{}{}".format(i + magnitude, plural_or_not, comma_or_dot), end=" ")
