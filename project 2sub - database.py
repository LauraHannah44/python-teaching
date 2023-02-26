db_string = open("project 2 database.txt", "r").read()

#string_part.join(list) => string
#"\n".join(("a", "b", "c")) => "a\nb\nc"

#string.split(string_part) => list
#"a\nb\nc".split("\n") => ("a", "b", "c")
user_list = list()

#for user_info in db_string.split("\n"):
#    user_list.append(user_info.split(" | "))

#user_list = [user_info.split(" | ") for user_info in db_string.split("\n")]

db_string = open("project 2 database.txt", "r").read()
user_strings = db_string.split("\n")  # list of one string per user
key_list = user_strings[0].split(" | ")  # the first string converted into a list (for the keys for each user dictionary)
del user_strings[0]  # remove first (keys) entry
for user_string in user_strings:  # iterating through each user's string
    user_info_list = user_string.split(" | ")  # converting each string to a list
    user_dict = dict()  # creating temporary dict to store keys and info (to be appended)
    for i, info in enumerate(user_info_list):  # each piece of user info for a single user
        user_dict[key_list[i]] = info  # creating a new dictionary entry with the corresponding key
    user_list.append(user_dict)  # appending that particular users dict to the full list

print(user_list)
