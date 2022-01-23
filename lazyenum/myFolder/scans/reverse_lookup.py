import subprocess

def reverse_lookup(target):
    command = f"dig -x {target} @{target} \n"
    com = subprocess.call(command, shell=True)
    return com
