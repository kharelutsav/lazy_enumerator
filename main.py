from concurrent.futures import ThreadPoolExecutor
import pyfiglet
from datetime import datetime
import socket
from multiprocessing import Process
import sys
import subprocess
from controller import controller
import test

###############################################################################


class Main:
    def __init__(self, ports, target, wordlists, tools):
        self.ports = ports
        self.target = target
        self.open_ports = []
        self.wordlists = wordlists
        self.tools = tools

    def serviceScan(self, port):
        command = f"nmap -sVC -p {port} -T4 {self.target} > ./{port}.txt"
        subprocess.call(command, shell=True)
        controller(self.target, port, wordlists, tools)
        # print(f"Port {port} open in {self.target}")
        # print(f"Starting nmap scan at port {port} \n")

    def scan(self, port):
        try:
            # will scan specified port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((self.target, port))
            if result == 0:
                self.open_ports.append(port)
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

    args = test.Parse_Arguments()
    wordlists = args.wordlists
    tools = args.tools

    ports = [21,22,23,25,80,88,110,111,137,138,139,443,445,668,1000]
    target = '127.0.0.1'
    start_time = datetime.now()
    # Add Banner
    ascii_banner = pyfiglet.figlet_format("LAZY ENUMERATOR")
    print(ascii_banner)
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scan started at: " + str(start_time))
    print("-" * 50)

    main = Main(ports, target, wordlists, tools)
    main.runner()

    end_time = datetime.now()
    if len(main.open_ports) == 0:
        print("No open ports found. \nCancelling enumeration process....")

    else:
        print(f"Scan finished at: {str(end_time)}")
        print(f"Open ports found: {main.open_ports}")
