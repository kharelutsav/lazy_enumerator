import subprocess

def http(ip):
    try:
        print("\nRunning [Whatweb]\n")
        command = f"whatweb -a 1 -v http://{ip} -U 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0'  >> 80.txt\n\n"
        comm = subprocess.call(command, shell=True)
    except:
        print("an error occured lease check manually whether the port is open or not or verify the service")
    try:
        command = f"ffuf -u http://{ip}/FUZZ -w /usr/share/dirb/wordlists/common.txt -e .php,.txt,.html -c -t 100 | tee httpdirstxt >> 80.txt \n\n"
        com = subprocess.call(command, shell=True)
    except:
        print("an error occured please check manually wheter the port is open or not or verify the service")
    return comm,com
