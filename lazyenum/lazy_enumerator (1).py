import socket
import threading
import sys
from queue import Queue
import subprocess
from webfuzzer import *
import ftplib

target = input('enter ip: ')
queue = Queue()
# port = 1000
open_port =[]
conn = ftplib.FTP()   # for ftp connection

try:
    default=0
    print("----Options to perform port scanning are:")
    print("1 to scan well known ports \n or enter port number upto which u want to perform scan \n 2 to scan most used ports like (21,80,443,445,1433,3306,5432 etc.) \n0 to scan all ports")
    portnums = int(input("Enter any of the above options to perform scan : "))
    if portnums==1:
        nums=range(1,1024)
    elif portnums==0:
        nums=range(1,65535)
    elif portnums==2:
        nums = (21,23,25,53,80,88,111,137,138,139,389,443,445,464,636,749,750,751,761,1433,3268,3269,3306,5432, 27017,27018,27019)
    elif default <= portnums:
        nums= range(1,portnums)
except:
    print("bad value")
    print("----Usage----")
    print("enter integers only: 100,1024,65335")

command = f"clear"
com = subprocess.call(command, shell=True)
