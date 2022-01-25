import subprocess

def dns_zonetransfer(target):
    print("Trying zone transfer without domain name \n")
    command = f"dig axfr @{target} \n"
    com = subprocess.call(command, shell=True)
    return com
