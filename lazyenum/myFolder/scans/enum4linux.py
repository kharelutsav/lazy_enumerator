import subprocess

def enum4linux(ip):
    command = f'\nenum4linux -a -u "" -p "" {target} \n&& enum4linux -a -u "guest" -p "" {target} \n | tee enum4linux.txt \n'
    com = subprocess.call(command, shell=True)
    return com
