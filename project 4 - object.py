def cut_string(string1, string2):
    #cuts the matching part of string1 from string2
    new_string2 = string2
    current_word = ""
    article = ("a ", "an ", "the ")

    for digit_index, string_digit in enumerate(string1):
        if string_digit == string2[digit_index]:

            current_word += string_digit

            if string_digit == " ":

                if current_word not in article:
                    new_string2 = string2[digit_index + 1:len(string2)]
                    current_word = ""

                else:
                    current_word = ""

        else:
            return new_string2

    return string2


class game_item:

    def __init__(self, name=None, colour=None, shape=None, temperature=None, texture=None, made_in=None, made_by=None, years_old=None, misc_descriptors=None):
        self.name = name

        #appearance
        self.colour = colour
        self.shape = shape

        #feel
        self.temperature = temperature
        self.texture = texture

        #origin
        self.made_in = made_in
        self.made_by = made_by
        self.years_old = years_old

        #misc
        self.misc_descriptors = misc_descriptors

    def describe(self, name=True, see=True, feel=True, know=True, detail=True):
        name_string = "This {}".format((self.name, "thing")[not self.name or not name])
        appearance_strings = list()
        feel_strings = list()
        origin_strings = list()
        string_sets = list()

        if see:
            if self.colour:
                appearance_strings.append("is {}".format(self.colour))
            if self.shape:
                appearance_strings.append("is {}".format(self.shape))

        pain = False

        if feel:
            #Needs to be checked as not False because otherwise 0 temp is taken as False.
            if self.temperature is not None:
                pain = pain or self.temperature >= 70 or self.temperature <= 0

                if self.temperature <= 0:
                    temperature_string = "freezing"
                elif self.temperature <= 15:
                    temperature_string = "cold"
                elif self.temperature <= 20:
                    temperature_string = "cool"
                elif self.temperature <= 35:
                    temperature_string = "normal"
                elif self.temperature <= 50:
                    temperature_string = "warm"
                elif self.temperature <= 100:
                    temperature_string = "hot"
                else:
                    temperature_string = "scalding"

                feel_strings.append("is {} to the touch".format(temperature_string))

            if self.texture:
                pain = pain or self.texture == "sharp" or self.texture == "prickly"

                feel_strings.append("feels {} in your fingers".format(self.texture))

        if know:
            if self.made_in:
                origin_strings.append("was made in {}".format(self.made_in))
            if self.made_by:
                origin_strings.append("was made by {}".format(self.made_by))

            if self.years_old == 0:
                origin_strings.append("is new")
            elif self.years_old:
                origin_strings.append("is {} year{} old".format(self.years_old, ("s", "")[self.years_old == 1]))
            else:
                if origin_strings:
                    origin_strings.append("its age is unknown")

        if appearance_strings:
            string_sets.append(appearance_strings)
        if feel_strings:
            string_sets.append(feel_strings)
        if origin_strings:
            string_sets.append(origin_strings)
        if self.misc_descriptors and detail:
            string_sets.append(self.misc_descriptors)

        final_string = False

        for set_num, string_set in enumerate(string_sets):

            #initial string_set gets name_string vs pronoun
            if set_num == 0:
                final_string = "{} ".format(name_string)
            else:
                final_string += "It "

            for string_num, current_string in enumerate(string_set):

                #end if only one string
                if len(string_set) == 1:
                    final_string += "{}. ".format(current_string)
                    if pain and string_set == feel_strings:
                        final_string += "Ouch! "

                #first string of set
                elif string_num == 0:
                    final_string += "{}, ".format(current_string)

                else:
                    string_check = cut_string(string_set[string_num - 1], current_string)

                    #multiple strings end
                    if string_num == len(string_set) - 1:
                        final_string += "and {}. ".format(string_check)
                        if pain and string_set == feel_strings:
                            final_string += "Ouch! "

                    #multiple strings mid
                    else:
                        final_string += "{}, ".format(string_check)

        if final_string:
            print(final_string)
        else:
            final_string = "{} is a mystery.".format(name_string)
            print(final_string)


item = game_item(name="chair", colour="blue", temperature=50, texture="sharp", made_by="Eve", years_old=8)
#game_item.__init__(item, "name", etc)

item.describe()
#game_item.describe(item)
