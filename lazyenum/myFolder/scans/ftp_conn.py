import subprocess

def ftp_conn(target):

    value = f'{target}'
    conn.connect(value, 21)
    print("Do u want to use default anonymous login try or enter ur own credential \n")
    print("[1] for default and [2] for entering ur own credential \n")
    take_creds = int(input("Enter ur choice : "))

    if take_creds == 1:
        try:
            conn.login('anonymous', 'anonymous')
            print(conn.pwd())
            print(conn.dir())
            ftp_contorller()


        except ftplib.all_errors as e:
            print("Default anonymous credential not accepted \n")

    elif take_creds == 2:
        usrname = input("Enter the username : ")
        paswod = input("Enter the paswd : ")
        try:
            print(conn.pwd())
            print(conn.dir())
            ftp_contorller()
        except ftplib.all_errors as e:
            print("Given credential not accepted \n")

    else:
        print("[WRONG] input choices \n")

