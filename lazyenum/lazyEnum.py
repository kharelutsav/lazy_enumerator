import socket
import threading
import sys
from queue import Queue
import subprocess
from datetime import datetime
from webfuzzer import *
import ftplib

target = input('enter ip: ')
queue = Queue()
# port = 1000
open_port =[]
conn = ftplib.FTP()   # for ftp connection

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        
        sock.connect((target,port))
        
    
        return True
    
    except:
        return False
        
closed_port = []        

def fill_queue(nums):
    for port in nums:
        queue.put(port)

def scanning_port():
    while not queue.empty():
        port = queue.get()
        # print(total)
        if portscan(port):
            print(f'\nPort open at {port}')
            open_port.append(port)
        else:
            print(f'\n Port closed at {port}')
            closed_port.append(port)

t1 =datetime.now()
def scanner():
    print("\nScanner started at \t",t1)
    fill_queue(nums)

    thread_list = []
    
    for t in range(1000):  #thread /speed
        thread = threading.Thread(target=scanning_port)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

try:
    default=0
    print("----Options to perform port scanning are:")
    print("1 to scan well known ports \n or enter port number upto which u want to perform scan \n 2 to scan most used ports like (21,80,443,445,1433,3306,5432 etc.) \n0 to scan all ports")
    portnums = int(input("Enter any of the above options to perform scan : "))
    if portnums==1:
        nums=range(1,1024)
    elif portnums==0:
        nums=range(1,65535)
    elif portnums==2:
        nums = (21,23,25,53,80,88,111,137,138,139,389,443,445,464,636,749,750,751,761,1433,3268,3269,3306,5432, 27017,27018,27019)
    elif default <= portnums:
        nums= range(1,portnums)
except:
    print("bad value")
    print("----Usage----")
    print("enter integers only: 100,1024,65335")

scanner()

t2 = datetime.now()
print("Finished at ", t2)
total = t2 - t1

command = f"clear"
com = subprocess.call(command, shell=True)

sorted_ports = open_port.sort()
print("\nScanning Completed in ", total)
print(f'Open ports are: {sorted_ports}\n')

num_of_closed = len(closed_port) + 1
print(f"Total number of closed port are {num_of_closed}\n\n")



#if 80 in open_port:
def http(ip):
    try:
        print("\nRunning [Whatweb]\n")
        command = f"whatweb -a 1 -v http://{target} -U 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0' \n\n"
        comm = subprocess.call(command, shell=True)
    except:
        print("an error occured lease check manually whether the port is open or not or verify the service")
    try:
        command = f"ffuf -u http://{ip}/FUZZ -w /usr/share/dirb/wordlists/common.txt -e .php,.txt,.html -c -t 100 | tee httpdirstxt \n\n"
        com = subprocess.call(command, shell=True)
    except:
        print("an error occured please check manually wheter the port is open or not or verify the service")
    return comm,com

def passive_webrecon(target):
    return

def gau_recon(target):
    return

def https(ip):
    print("\n[Whatweb]\n")
    command = f"whatweb -a 1 -v https://{target} -U 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0' \n\n"
    coom = subprocess.call(command,shell =True)
    command = f"ffuf -u https://{ip}/FUZZ -w /usr/share/dirb/wordlists/common.txt -e .php,.txt,.html -c -t 100 \n | tee httpsdirs.txt"
    com = subprocess.call(command, shell=True)
    return com

def nikto(ip):
    command = f"\nnikto -h {ip} | tee nikto.txt \n"
    com = subprocess.call(command, shell=True)
    return com

def smbclient(ip):
    command = f"\nsmbclient -N -L \\\\{ip}\n"
    com = subprocess.call(command, shell=True)
    return com

def enum4linux(ip):
    command = f'\nenum4linux -a -u "" -p "" {target} \n&& enum4linux -a -u "guest" -p "" {target} \n | tee enum4linux.txt \n'
    com = subprocess.call(command, shell=True)
    return com

def ftp_contorller():
    print("\nDo u wanna dowload file or change directory\n")
    print("If u wanna download file enter [1] else [2] for change directory and [3] to ignore ftp")
                
    while True:
        usr_choice = int(input("Enter ur choice : "))
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


def ssh_passbf(user,target):
    print("\nUsing '/usr/share/wordlists/rockyou.txt' wordlists for password bruteforce")
    command = f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {target} ssh -t 30\n" 
    com = subprocess.call(command, shell=True)
    return com

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

def telnet_bannergrab(target):
    command=f"nc -vn {target} \n"
    com = subprocess.call(command, shell=True)
    return com

def dns_zonetransfer(target):
    print("Trying zone transfer without domain name \n")
    command = f"dig axfr @{target} \n"
    com = subprocess.call(command, shell=True)
    return com

def reverse_lookup(target):
    command = f"dig -x {target} @{target} \n"
    com = subprocess.call(command, shell=True)
    return com

def showmount(target):
    command = f"showmount -e {target} \n"
    com = subprocess.call(command, shell=True)
    return com


while len(open_port) !=0:
    for i in open_port:
    #ports_for_nmap = seperator.join(open_port)
        command = f"nmap -sVC -p {i} -T4 {target}"
        com = subprocess.call(command, shell=True)
    
    
    print(f"\nOpen port : {open_port}")
    print("\n'd' for http/https directory enumeration & nikto enumeration")
    print("'s' for smb/samba enumeration")
    print("'a' for every kind of enumeration\n")
    some_input = input("Enumeration to be performed. Chose ur options...!!!: ")

    if some_input == "d":
        if 80 in open_port:
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
    
        if 443 in open_port:
            https(target)
            print("\n\nDo you wanna run nikto too????")
            while True:
                ask_usr = input("Enter [y] to run nikto or [n] to cancel : \n")
                if ask_usr == "y":
                    nikto(target)
                elif ask_usr == "n":
                    PRINT("[EXITING]")
                    break
                else:
                    print("\nBad Input..... Try entering 'y' or 'n' only")
    
    elif some_input == "s":
        if 445 in open_port:
            enum4linux(target),smbclient(target
                    )
    elif some_input == "a":
        if 21 in open_port:
            ftp_conn(target)
        
        if 22 in open_port:
            print("SSH brute forcing using hydra!!!!   HAIL HYDRA....")
             
        if 80 in open_port:
            http(target)
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

        
        if 111 in open_port:
            showmount(target)

        if 443 in open_port:
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

       
        if 445 in open_port:
            enum4linux(target),smbclient(target)

    else:
        print("wrong choice .. Do whatever u want now.. xD")
    break 
    #if 445 in open_port:
     #  enum4linux(target),smbclient(target)
       #break



if len(open_port) ==0:
    print("No open ports found so .. Cancelling the enumeration process....")

