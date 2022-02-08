import subprocess

def showmount(target):
    command = f"showmount -e {target} >> showmount.txt"
    subprocess.call(command, shell=True)
