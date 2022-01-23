import subprocess

def smbclient(ip):
    command = f"\nsmbclient -N -L \\\\{ip}\n"
    com = subprocess.call(command, shell=True)
    return com
