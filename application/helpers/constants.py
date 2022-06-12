import random, requests, getmac, socket
import subprocess as sp

# ----------------------------------------------------------------------------------

try:
    PUB_IP = requests.get('https://ident.me').text
except Exception as e:
    PUB_IP = "NA. Error Occured."

PRI_IP = socket.gethostbyname(socket.gethostname())
MAC = getmac.get_mac_address()
HOST = sp.getoutput("hostname")
USER = sp.getoutput("whoami")

DISK = sp.getoutput("wmic logicaldisk get size,freespace,caption").replace("\n\n", "\n")

# ----------------------------------------------------------------------------------
    
WELCOME_MSG = "Welcome, {}!".format(USER.split('\\')[1].title())

LEFT_STATUS_LABEL = "☀ {}  ⚡ {}%   🧠 {}/{}GB ({}%)   💾 {}/{}TB ({}%)%"
RIGHT_STATUS_LABEL = "{} {}%"

# ----------------------------------------------------------------------------------

SYSTEM = '\n'+'Last Bootup Time: {}'+'\n\n'+DISK+"""CPU Usage: {}%   |   RAM Usage: {}%

Battery: {}% {}"""

# ----------------------------------------------------------------------------------

NETWORK = """
Host: {}

User: {}

Public IP: {}

Private IP: {}

MAC Address: {}
""".format(HOST, USER, PUB_IP, PRI_IP, MAC)

# ----------------------------------------------------------------------------------

ABOUT = """
Afterlife is a minimalistic HUD.

It brings all the important functions/commands of Windows to the fingertips of its users. It also highlights some of the popular internet services/utilities.

Made with ♥ by a_ignorant_mortal
""".strip()

# ----------------------------------------------------------------------------------

WIKI = """
Title - {}
Article URL - {}

Summary - {}

Error - {}
"""
