import subprocess

def enum4linux(target):
    command = f'enum4linux -a -u "" -p "" {target} >> enum4linux.txt && enum4linux -a -u "guest" -p "" {target} >> enum4linux.txt'
    subprocess.call(command, shell=True)
