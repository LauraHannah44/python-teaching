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


print(cut_string("he likes green eggs", "he likes green ham"))

#both same through and after whitelisted article
print(cut_string("she's a fan of the teacher", "she's a fan of the mathmatician"))
#expected output: "brown"

#whitelisted article followed by same-starting
print(cut_string("she's a teacher", "she's a mathmatician"))
#expected output: "a brown"

#both different
#print(cut_string("he's broken", "she's brown"))
#expected output: "she's brown"

#both same until space
#print(cut_string("it's broken", "it's not broken"))
#expected output: "not broken"

#both same through multiple words
#print(cut_string("it is broken", "it is not broken"))
#expected output: "not broken"

#both same through space until midword
#print(cut_string("it's broken", "it's brown"))
#expected output: "brown"

#both identical
#print(cut_string("he's broken", "he's broken"))
#expected output: "he's broken"
