import os
import sys
import time
from os import system
from time import sleep

try:
    import requests
except ImportError:
    os.system('pip3 install requests')

try:
    request = requests.get("https://www.google.com/search?q=tahmid+rayat", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] No internet connection [!]")
    sys.exit()

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """
\033[1;32m  ______    _         \033[1;33m  __  __       _ _           
\033[1;32m |  ____|  | |        \033[1;33m |  \/  |     (_) |          
\033[1;32m | |__ __ _| | _____  \033[1;33m | \  / | __ _ _| | ___ _ __ 
\033[1;32m |  __/ _  | |/ / _ \ \033[1;33m | |\/| |/ _  | | |/ _ \  __|
\033[1;32m | | | (_| |   <  __/ \033[1;33m | |  | | (_| | | |  __/ |   
\033[1;32m |_|  \__,_|_|\_\___| \033[1;33m |_|  |_|\__,_|_|_|\___|_|   

\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m CREATED BY HTR-TECH \033[1;31m(\033[1;33mTAHMID RAYAT\033[1;31m)
"""

system("clear")
print (logo)
print ('')
hprint(G + ' Launching Fake Mailer ...')
sleep(2)
print ('')
to = input(G + " Send Mail To" + C + " : " + Y)
print ('')
subject = input(G + " Input Mail Subject" + C + " : " + Y)
print ("")
msg = input(G + " Input Mail Content" + C + " : " + Y)
print ("")
usagnt = 'Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV
