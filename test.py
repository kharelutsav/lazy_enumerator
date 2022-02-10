from sys import argv


class Parse_Arguments:
    def __init__(self):
        self.tools = {'web_tool': 'gobuster', 'subdomain_tool': 'default'}
        self.wordlists = {'web_wordlist': '/usr/share/dirb/wordlists/common.txt', 'subdomoain_wordlist': 'default'}
        self.target = {}
        self.parse()
        if len(self.target) == 0:
            print("\
    \n!!!!!!!!! Target not specified !!!!!!!!!!\n\n\
Examples:\n\
    app --ip 127.0.0.1\n\
    app --domain example.com --dir_wl /path/to/wordlists --dir_t preferred_tool_name\n\
                ")
            exit(2)
        elif len(self.target) > 1:
            print("\
    \n!!!!!!!!! Please provide one of ip address or domain name !!!!!!!!!!\n\n\
Examples:\n\
    app --ip 127.0.0.1\n\
    app --domain example.com --dir_wl /path/to/wordlists --dir_t preferred_tool_name\n\
                ")
            exit(2)


    def parse(self):
        for i in range(len(argv)):
            if argv[i] == '--dir_wl':
                self.wordlists['web_wordlist'] = argv[i + 1]
            if argv[i] == '--ssh-user-bf':
                self.wordlists['ssh_user'] = argv[i + 1]
            if argv[i] == '--dir_t':
                self.tools['web_tool'] = argv[i + 1]
            if argv[i] == '--sub_domain_wl':
                self.wordlists['subdomoain_wordlist'] = argv[i + 1]
            if argv[i] == '--sub_domain_t':
                self.tools['subdomain_tool'] = argv[i + 1]
            if argv[i] == '--help' or argv[i] == '-h':
                with open('help.txt', 'r') as help:
                    for i in help.readlines():
                        text = i[0:-1]
                        print(text)
                    exit(0)
            if argv[i] == '--ip':
                self.target['ip'] = argv[i + 1]
            elif argv[i] == '--domain':
                self.target['domain'] = argv[i + 1]
