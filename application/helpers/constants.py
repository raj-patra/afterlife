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
ART_ICON="./assets/icons/art.png"
BATTERY_ICON="./assets/icons/battery.png"
BOOK_ICON="./assets/icons/book.png"
BRAIN_ICON="./assets/icons/brain.png"
CALENDAR_ICON="./assets/icons/calendar.png"
CAMERA_ICON="./assets/icons/camera.png"
CLOCK_ICON="./assets/icons/clock.png"
DISPLAY_ICON="./assets/icons/display.png"
DIVISION_ICON="./assets/icons/division.png"
EMAIL_ICON="./assets/icons/email.png"
FLOPPY_DISK_ICON="./assets/icons/floppy_disk.png"
GEAR_ICON="./assets/icons/gear.png"
HIGH_BRIGHTNESS_ICON="./assets/icons/high_brightness.png"
INTERNET_ICON="./assets/icons/internet.png"
LOCK_ICON="./assets/icons/lock.png"
MAG_RIGHT_ICON="./assets/icons/mag_right.png"
MAPS_ICON="./assets/icons/maps.png"
MESSAGES_ICON="./assets/icons/messages.png"
MUSIC_ICON="./assets/icons/music.png"
NETWORK_ICON="./assets/icons/network.png"
ROBOT_ICON="./assets/icons/robot.png"
SCISSORS_ICON="./assets/icons/scissors.png"
SELFIE_ICON="./assets/icons/selfie.png"
SPIRAL_NOTE_PAD="./assets/icons/spiral_note_pad.png"
VIDEO_ICON="./assets/icons/video.png"
WEATHER_ICON="./assets/icons/weather.png"
X_ICON="./assets/icons/x.png"
ZAP_ICON="./assets/icons/zap.png"
