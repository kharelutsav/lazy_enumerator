import subprocess

def showmount(target):
    command = f"showmount -e {target} \n"
    com = subprocess.call(command, shell=True)
    return com
