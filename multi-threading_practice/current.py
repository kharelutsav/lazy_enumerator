from concurrent import futures
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import sleep
import os
import pyfiglet
import sys
import socket
from datetime import datetime


def portsScan(port, target):

   try:
      # will scan specified port
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      
      # returns an error indicator
      result = s.connect_ex((target,port))
      if result == 0:
         print("Port {} is open".format(port))

      s.close()
         
   except KeyboardInterrupt:
         print("\n Exiting Program !!!!")
         sys.exit()
   except socket.gaierror:
         print("\n Hostname Could Not Be Resolved !!!!")
         sys.exit()
   except socket.error:
         print("\ Server not responding !!!!")
         sys.exit()

def task(message, port, target):
   portsScan(port, target)

ports = 1000

def main():
   ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
   print(ascii_banner)

   # Defining a target
   if len(sys.argv) == 2:
      
      # translate hostname to IPv4
      target = socket.gethostbyname(sys.argv[1])
   else:
      print("Invalid amount of Argument")
   # Add Banner
   print("-" * 50)
   print("Scanning Target: " + target)
   print("Scanning started at:" + str(datetime.now()))
   print("-" * 50)

   
   with ThreadPoolExecutor(100) as executor:
      for port in range(ports):
         executor.submit(task, *('Completed', port, target))

   
if __name__ == '__main__':
   main()
