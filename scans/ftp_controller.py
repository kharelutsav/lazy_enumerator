import ftplib
conn = ftplib.FTP()

def ftp_contorller():
        if usr_choice == 1:
            filename = input("Enter the file name to download: ")
            try:
                with open(filename, "wb") as file:

                    conn.retrbinary(f"RETR {filename}", file.write)

            except ftplib.all_errors as e:
                print("wrong filename or error occured\n")

        elif usr_choice ==2 :
            try:
                print("To change directory enter the directory name")
                dirs = input("enter the dir name : ")
                print(conn.cwd(f"/{dirs}"))

                print(conn.dir())

            except ftplib.all_errors as e:
                print("wrong path or error occured\n")

        elif usr_choice == 3:
            print("Ignoring ftp port")

        else:
            print("wrong choice")
        conn.quit()
        break
