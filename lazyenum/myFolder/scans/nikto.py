import subprocess

def nikto(ip):
    command = f"\nnikto -h {ip} | tee nikto.txt \n"
    com = subprocess.call(command, shell=True)
    return com
