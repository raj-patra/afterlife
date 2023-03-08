import subprocess as sp

# ----------------------------------------------------------------------------------

USER = sp.getoutput("whoami")

# ----------------------------------------------------------------------------------
    
WELCOME_MSG = "Welcome, {}!".format(USER.split('\\')[1].title())

LEFT_STATUS_LABEL = "☀ {}  ⚡ {}%   🧠 {}/{}GB ({}%)   💾 {}/{}TB ({}%)%"
RIGHT_STATUS_LABEL = "Uptime: {} | {} {}% |"

# ----------------------------------------------------------------------------------

ABOUT = """
Welcome to the Afterlife!

Afterlife is a minimalistic HUD.

It brings all the important functions/commands of Windows to the fingertips of its users. 

It also highlights some of the popular internet services/utilities.

Made with ♥ by a_ignorant_mortal
""".strip()

# ----------------------------------------------------------------------------------

WIKI = """
Here's your article...

Title - {}
Article URL - {}

Summary

{}
"""
