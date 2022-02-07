import subprocess

def http(ip, tool, wordlist):
    try:
        with open('80.txt', 'a') as file:
            file.write('\n\n WhatWeb Result \n\n')
        command = f"whatweb -a 1 -v http://{ip} -U 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'  >> 80.txt"
        subprocess.call(command, shell=True)
    except:
        print("an error occured please check manually wheter the port is open or not or verify the service")

    with open('80.txt', 'a') as file:
            file.write(f'\n\n {tool} Result \n\n')

    if tool == 'ffuf':
        try:
            command = f"ffuf -u http://{ip}/FUZZ -w {wordlist} -e .php,.txt,.html -c -t 100 >> 80.txt"
            subprocess.call(command, shell=True)
        except:
            print("an error occured please check manually wheter the port is open or not or verify the service")

    elif tool == 'dirsearch':
        if wordlist == '/usr/share/dirb/wordlists/common.txt':
            try:
                command = f"dirsearch -u http://{ip} -r -t 100 >> 80.txt"
                subprocess.call(command, shell=True)
            except:
                print("an error occured please check manually wheter the port is open or not or verify the service")
        else:
            try:
                command = f"dirsearch -u http://{ip} -w  {wordlist} -r -t 100 >> 80.txt"
                subprocess.call(command, shell=True)
            except:
                print("an error occured please check manually wheter the port is open or not or verify the service")

    else:
        try:

            command = f"gobuster dir -u http://{ip} -w {wordlist} -x .php,.txt,.html -t 100 -q >> 80.txt"
            subprocess.call(command, shell=True)
        except:
            print("an error occured please check manually wheter the port is open or not or verify the service")
