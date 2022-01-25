from scans.nikto import nikto
from scans.http import http
from scans.https import https


class Directory_Enumerator:
    """
    Enumerates for directory.
    """
    def __init__(self):
        pass

    def enum(port, target):
        if port == 80:
            http(target)
            print("\n\nDo you wanna run niktoo too????")
            while True:
                ask_usr = input("Enter [y] to run nikto or [n] to cancel : \n")
                if ask_usr == "y":
                    nikto(target)
                elif ask_usr == "n":
                    print("[EXITING")
                    break
                else:
                    print("\nBad Input..... Try entering 'y' or 'n' only")
        if port == 443:
            https(target)
            print("\n\nDo you wanna run nikto too????")
            while True:
                ask_usr = input("Enter [y] to run nikto or [n] to cancel : \n")
                if ask_usr == "y":
                    nikto(target)
                elif ask_usr == "n":
                    print("[EXITING]")
                    break
                else:
                    print("\nBad Input..... Try entering 'y' or 'n' only")
