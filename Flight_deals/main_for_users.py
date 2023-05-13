from sheety import SheetyManager

sheety_manager = SheetyManager()
add_user = True

print("Welcome to Illia's Flight club!")
print("We find the best flights deals and email you.")

user_first_name = input("What is your first name?\n")
user_last_name = input("What is your last name?\n")

all_users = sheety_manager.get_all_users()
print(all_users)

while add_user:
    user_email = input("What is your email?\n")
    email_confirm = input("Type your email again.\n")

    if len(all_users) > 0:
        if user_email == email_confirm:
            for item in all_users:
                if user_email == item['email']:
                    print("This Email alredy used")
                else:
                    sheety_manager.add_user(first_name=user_first_name,
                                            last_name=user_last_name,
                                            email=user_email)
                    print("You're in the Club!")
                    add_user = False
        elif user_email != email_confirm:
            print("Entered emails didn't match")
    else:
        if user_email == email_confirm:
            sheety_manager.add_user(first_name=user_first_name,
                                    second_name=user_last_name,
                                    email=user_email)
            print("You're in the Club!")
            add_user = False
        elif user_email != email_confirm:
            print("Entered emails didn't match")
