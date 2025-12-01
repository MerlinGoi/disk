import os

import GUI
import search_tg_user as srch_tg_us
import send_sms as snd_msg
#import db_functions as db_func


def get_user_input():
    while True:
        try:
            option = int(input("Please enter an option: "))
            if option == 1:
                cls()

            elif option == 2:
                cls()
                return option

            elif option == 3:
                cls()
                return option

            elif option == 4:
                cls()
                return option

            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    GUI.interface()
    selected_option = get_user_input()
    if selected_option == 1:
        print(srch_tg_us.phone_vlidation())

    elif selected_option == 2:
        snd_msg.send_sms()

    elif selected_option == 3:
        db_func.read_users()

    elif selected_option == 4:
        db_func.find_users_by_fio()

    else:
        print("nothing chosen...")

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

    a = int(input("||       1 - close       ||      2 - return      ||\n\nyour option: "))
    if a == 2:
        if __name__ == "__main__":
            main()


if __name__ == "__main__":
    main()



