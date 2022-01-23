from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import pyfiglet
import sys
from datetime import datetime
from portScan import *

import subprocess

###############################################################################
import ftplib

conn = ftplib.FTP()   # for ftp connection


###############################################################################

def task(port, target):
   portsScan(port, target)

ports = [21,22,23,25,80,88,110,111,137,138,139,443,445,668,1000]

def main():
   ascii_banner = pyfiglet.figlet_format("LAZY ENUMERATOR")
   print(ascii_banner)

   # Defining a target
   target = '127.0.0.1'

   # Add Banner
   print("-" * 50)
   print("Scanning Target: " + target)
   print("Scanning started at:" + str(datetime.now()))
   print("-" * 50)

   
   with ThreadPoolExecutor(100) as executor:
      for port in ports:
         executor.submit(task, *(port, target))

   
if __name__ == '__main__':
   main()
