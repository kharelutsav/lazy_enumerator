import subprocess

def sublist(domain):
    print("Sublist3r is starting")
    command = f"sublist3er -d {domain} >> sublister.txt"
    subprocess.call(command,shell=True)
