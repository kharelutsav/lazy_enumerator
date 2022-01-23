import socket
from multiprocessing import Process
import sys

def serviceScan(target, port):
   print(f"Port {port} open in {target}")
   print(f"Starting nmap scan at port {port} \n")

def portsScan(port, target):

   try:
      # will scan specified port
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)
      
      # returns an error indicator
      result = s.connect_ex((target,port))
      if result == 0:
         q = Process(target=serviceScan, args=(target, port))
         q.start()
         
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