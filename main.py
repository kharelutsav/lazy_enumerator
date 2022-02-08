import asyncio, test, sys, subprocess, socket, pyfiglet, os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from multiprocessing import Process
from controller import controller
###############################################################################


class extra:
    def __init__(self, start_time):
        args = test.Parse_Arguments()
        self.wordlists = args.wordlists
        self.tools = args.tools
        self.target = args.target['ip'] if 'ip' in args.target else args.target['domain']
        self.popular_ports = [21,22,23,25,80,88,110,111,137,138,139,443,445,668,1000]
        self.selected_ports = []
        self.start_time = start_time

    def banner(self):
        # Add Banner
        ascii_banner = pyfiglet.figlet_format("LAZY ENUMERATOR")
        print(ascii_banner)
        print("-" * 50)
        print("Scanning Target: " + self.target)
        print("Scan started at: " + str(self.start_time))
        print("-" * 50)


class Main(extra):
    def __init__(self, start_time):
        super().__init__(start_time)
        self.open_ports = []

    def serviceScan(self, port):
        command = f"nmap -sVC -p {port} -T4 {self.target} > ./{port}.txt"
        subprocess.call(command, shell=True)
        controller(self.target, port, self.wordlists, self.tools)
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
            for port in self.popular_ports:
                executor.submit(self.scan, port)

def run():
    try:
        start_time = datetime.now()
        main = Main(start_time)

        main.banner()
        main.runner()

        end_time = datetime.now()

        if len(main.open_ports) == 0:
            print(f"Scan finished at: {str(end_time)}")
            print("No open ports found.")
        else:
            print(f"Scan finished at: {str(end_time)}")
            print(f"Open ports found: {main.open_ports}")

    except KeyboardInterrupt:
        os.kill(os.getpid(), 9)

def main():
	try:
		run()
	except asyncio.exceptions.CancelledError:
		pass
	except RuntimeError:
		pass

if __name__ == '__main__':
    main()
