from sys import argv


class Parse_Arguments:
    def __init__(self):
        self.tools = {'web_tool': 'gobuster', 'subdomain_tool': 'default'}
        self.wordlists = {'web_wordlist': '/usr/share/dirb/wordlists/common.txt', 'subdomoain_wordlist': 'default'}
        self.parse()

    def parse(self):
        for i in range(len(argv)):
            if argv[i] == '--dir_wl':
                self.wordlists['web_wordlist'] = argv[i + 1]
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

tools = Parse_Arguments().tools
wordlists = Parse_Arguments().wordlists

# C:/Python310/python.exe c:/Users/Killion/Desktop/lazy_enumerator/test.py --dir_wl /hello/fuck --dir_t what --sub_domain_wl haha --sub_domain_t stop
