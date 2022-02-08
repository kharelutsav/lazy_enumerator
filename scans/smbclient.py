import subprocess

def smbclient(ip):
    command = f"smbclient -N -L {ip} >> smb.txt"
    subprocess.call(command, shell=True)
