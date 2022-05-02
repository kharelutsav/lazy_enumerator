import subprocess

def gau(domain):
    print("gau is starting")
    command= f"gau {domain} >> gau.txt"
    subprocess.call(command, shell=True)
