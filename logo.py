
import os, sys, time
# Normal colors
yellow = "\033[0;33m"
white = "\033[0;37m"

# Bold colors
bred = "\033[1;31m"
bgreen = "\033[1;32m"
byellow = "\033[1;33m"
bblue = "\033[1;34m"
bpurple = "\033[1;35m"
bcyan = "\033[1;36m"
bwhite = "\033[1;37m"

# Use colors according to your wish

# Use https://fsymbols.com/generators/carty/ for your own font in banner

# If you use a custom banner from any site, you may use custombanner.py to add colors easily

logo='''
'''+bgreen+''' ____  ____  _   _ _   _  ___  
'''+bred+'''| __ )|  _ \| | | | \ | |/ _  \ 
'''+bcyan+'''|  _ \| |_) | | | |  \| | | | |
'''+byellow+'''| |_) |  _ <| |_| | |\  | |_| |
'''+bblue+'''|____/|_| \_\\___ /|_| \_|\____/ 
'''+bpurple+'''   Deguenon INT-2240 (Project)
'''+bgreen+'''           Network Automation
'''
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.09)

def slowprint2(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)


slowprint2(logo)
print(bgreen + 'Press Enter or any key to start the Auto configuration')
os.system('pause')
print(white)
