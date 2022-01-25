import subprocess

def telnet_bannergrab(target):
    command=f"nc -vn {target} \n"
    com = subprocess.call(command, shell=True)
    return com
