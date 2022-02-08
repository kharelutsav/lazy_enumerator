import subprocess
from scans.ssh_bf import ssh_bf
from scans.http import http
from scans.https import https
from scans.ftp_conn import ftp_conn
from scans.enum4linux import enum4linux
from scans.smbclient import smbclient
from scans.showmount import showmount

# class Controller:
#     def __init__(self, port, target, wordlists, tools):
#         self.port = port
#         self.target = target
#         self.wordlists = wordlists
#         self.tools = tools

#     def nmap(self):
#         command = f"nmap -sVC -p {self.port} -T4 {self.target}"
#         subprocess.call(command, shell=True)

#     def web(self):
#         http(self.target, self.tools.web_tool, self.wordlists.web_wordlist)
#         https(self.target)

#     def ftp(self):
#         ftp_conn(self.target)

#     def ssh():
#         print("SSH brute forcing using hydra!!!!   HAIL HYDRA....")

#     def samba(self):
#         enum4linux(self.target)
#         smbclient(self.target)
#         showmount(self.target)

def controller(target, port, wordlists, tools):
    if port == 80:
        http(target, tools['web_tool'], wordlists['web_wordlist'])
    elif port == 443:
        https(target)
    elif port == 21:
        ftp_conn(target)
    elif port == 22 and 'ssh_user' in wordlists:
        ssh_bf(target, wordlists['ssh_user'])
    elif port == 445:
        enum4linux(target)
        smbclient(target)
        showmount(target)
