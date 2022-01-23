from concurrent.futures import ThreadPoolExecutor
import pyfiglet
from datetime import datetime
import socket
from multiprocessing import Process
import sys

###############################################################################


class Main:
    def __init__(self, ports, target):
        self.ports = ports
        self.target = target

    def serviceScan(self, port):
        print(port)
        print(f"Port {port} open in {self.target}")
        print(f"Starting nmap scan at port {port} \n")

    def scan(self, port):
        try:
            # will scan specified port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((self.target, port))
            if result == 0:
                q = Process(target=self.serviceScan, args=(port,))
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

    def runner(self):
        with ThreadPoolExecutor(100) as executor:
            for port in self.ports:
                executor.submit(self.scan, port)


if __name__ == '__main__':
    ports = [21,22,23,25,80,88,110,111,137,138,139,443,445,668,1000]
    target = '127.0.0.1'

    # Add Banner
    ascii_banner = pyfiglet.figlet_format("LAZY ENUMERATOR")
    print(ascii_banner)
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    main = Main(ports, target)
    main.runner()
