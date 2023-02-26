login_database = [{"username": "user1", "password": "pass1", "email": "maskedlauraiscute", "attempts": 3},
                  {"username": "user2", "password": "pass2", "email": "short", "attempts": 3},
                  {"username": "user3", "password": "pass3", "email": "reallyreallylongemail32322", "attempts": 3}]


def mask_string(unmasked_string, masking_proportion=0.75):
    length = len(unmasked_string)
    masked_length = round(length * masking_proportion)
    half_unmasked_length = round((length - masked_length) / 2)

    string_start = unmasked_string[0:half_unmasked_length]
    string_end = unmasked_string[half_unmasked_length + masked_length:length]

    masked_string = string_start + "*" * masked_length + string_end
    return masked_string


logged_in = False
only_pass = False
portal_attempts = 3
out_of_attempts = False

while not logged_in:

    if not only_pass:
        username_input = input("Username\n")

    password_input = input("Password\n")

    for index, login_data in enumerate(login_database):
        user_correct = login_data["username"].lower() == username_input.lower()
        pass_correct = login_data["password"] == password_input
        pass_caseless_correct = login_data["password"].lower() == password_input.lower()
        if login_data["attempts"] is not None:
            if user_correct and pass_correct:
                logged_in = True
                portal_attempts = 5
                login_database[index]["attempts"] = 3
                print("Welcome {}!".format(login_data["username"]))
                break

            elif user_correct and pass_caseless_correct:
                only_pass = True
                login_database[index]["attempts"] -= 1
                print("Passwords are case sensitive. {} attempts remaining.".format(login_database[index]["attempts"]))
                break

            elif user_correct:
                only_pass = True
                login_database[index]["attempts"] -= 1
                print("Wrong password. {} attempts remaining.".format(login_database[index]["attempts"]))
                break

        else:
            if user_correct:
                print("User blocked due to failed login attempts.")
                break

    if login_database[index]["attempts"] == 0 and user_correct:

        masked_email = mask_string(login_database[index]["email"])

        print("Email sent to {}@companymail.com".format(masked_email))
        login_database[index]["attempts"] = None
        only_pass = False

    if not logged_in and not user_correct and not pass_caseless_correct:
        portal_attempts -= 1
        if portal_attempts == 0:
            print("Out of attempts, shutting down.")
            quit()
        print("Please try again. {} attempts remaining.".format(portal_attempts))

print("Logged in successfully.")
