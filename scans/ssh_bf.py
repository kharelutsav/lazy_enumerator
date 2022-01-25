import subprocess

def ssh_bf():
    print("\nDo u wanna brute force password")
    print("TO brute force type 'b' else 'p' to pass\n")
    usr_input = input("Enter ur choice : ")
    while True:
        if usr_input == 'b':
            ask_username = input("ENTER the username to brute force its password : ")
            if ask_username !=NULL:
                ssh_passbf(ask_username, target)
            else:
                print("Error on input or no username was given \n")
        elif usr_input == 'p':
            print("Ignorring ssh brute forcing \n")
            break
        else:
            print("Incorrect choice \n")
