import subprocess

def https(ip):
    print("\n[Whatweb]\n")
    command = f"whatweb -a 1 -v https://{target} -U 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0' \n\n"
    coom = subprocess.call(command,shell =True)
    command = f"ffuf -u https://{ip}/FUZZ -w /usr/share/dirb/wordlists/common.txt -e .php,.txt,.html -c -t 100 \n | tee httpsdirs.txt"
    com = subprocess.call(command, shell=True)
    return com
