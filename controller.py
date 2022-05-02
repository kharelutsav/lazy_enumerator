from scans.ssh_bf import ssh_bf
from scans.http import http
from scans.https import https
from scans.ftp_conn import ftp_conn
from scans.enum4linux import enum4linux
from scans.smbclient import smbclient
from scans.showmount import showmount
from scans.sublister import sublist
from scans.gau import gau
import re

regey = re.compile(r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")
def controller(target, port, wordlists, tools):
    if re.match(regey, target) == None:
        sublist(target)
        gau(target)
    elif port == 80:
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
    
