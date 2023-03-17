import subprocess as sp

# ----------------------------------------------------------------------------------

USER = sp.getoutput("whoami")

# ----------------------------------------------------------------------------------
    
WELCOME_MSG = "Welcome {}!".format(USER.split('\\')[1].title())

LEFT_STATUS_LABEL = "☀ {}  ⚡ {}%   🧠 {}/{}GB ({}%)   💾 {}/{}TB ({}%)"
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

# ----------------------------------------------------------------------------------

ARROW_FORWARD_ICON="./assets/icons/arrow_forward.png"
art="./assets/icons/art.png"
battery="./assets/icons/battery.png"
BOOK_ICON="./assets/icons/book.png"
brain="./assets/icons/brain.png"
calendar="./assets/icons/calendar.png"
camera="./assets/icons/camera.png"
clock="./assets/icons/clock.png"
display="./assets/icons/display.png"
division="./assets/icons/division.png"
email="./assets/icons/email.png"
floppy_disk="./assets/icons/floppy_disk.png"
gear="./assets/icons/gear.png"
high_brightness="./assets/icons/high_brightness.png"
internet="./assets/icons/internet.png"
lock="./assets/icons/lock.png"
MAG_RIGHT_ICON="./assets/icons/mag_right.png"
maps="./assets/icons/maps.png"
messages="./assets/icons/messages.png"
music="./assets/icons/music.png"
network="./assets/icons/network.png"
robot="./assets/icons/robot.png"
scissors="./assets/icons/scissors.png"
selfie="./assets/icons/selfie.png"
spiral_note_pad="./assets/icons/spiral_note_pad.png"
video="./assets/icons/video.png"
weather="./assets/icons/weather.png"
X_ICON="./assets/icons/x.png"
zap="./assets/icons/zap.png"
