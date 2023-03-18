"""Call to actions used in afterlife"""

from application.helpers import constants

SIDE_BAR_ACTIONS = [
    dict(event="start_app", icon="⏰", icon_file=constants.CLOCK_ICON, label="Alarms & Clock", query="start ms-clock:"),
    dict(event="start_app", icon="➗", icon_file=constants.DIVISION_ICON, label="Calculator", query="start calculator:"),
    dict(event="start_app", icon="📆", icon_file=constants.CALENDAR_ICON, label="Calendar", query="start outlook cal:"),
    dict(event="start_app", icon="📸", icon_file=constants.CAMERA_ICON, label="Camera", query="start microsoft.windows.camera:"),
    dict(event="start_app", icon="🤖", icon_file=constants.ROBOT_ICON, label="Cortana", query="start ms-cortana:"),
    dict(event="start_app", icon="🎶", icon_file=constants.MUSIC_ICON, label="Groove Music", query="start mswindowsmusic:"),
    dict(event="start_app", icon="📧", icon_file=constants.EMAIL_ICON, label="Mail", query="start outlookmail:"),
    dict(event="start_app", icon="🗺", icon_file=constants.MAPS_ICON, label="Maps", query="start bingmaps:"),
    dict(event="start_app", icon="🌐", icon_file=constants.INTERNET_ICON, label="Microsoft Edge", query="start microsoft-edge:"),
    dict(event="start_app", icon="🎥", icon_file=constants.VIDEO_ICON, label="Movies & TV", query="start mswindowsvideo:"),
    dict(event="start_app", icon="🗒", icon_file=constants.SPIRAL_NOTE_PAD, label="Notepad", query="start notepad"),
    dict(event="start_app", icon="🎨", icon_file=constants.ART_ICON, label="Paint", query="start mspaint"),
    dict(event="start_app", icon="🤳", icon_file=constants.SELFIE_ICON, label="Photos", query="start ms-photos:"),
    dict(event="start_app", icon="✂", icon_file=constants.SCISSORS_ICON, label="Snip & Sketch", query="start ms-ScreenSketch:"),
    dict(event="start_app", icon="⛅", icon_file=constants.WEATHER_ICON, label="Weather", query="start bingweather:"),
    dict(event="start_app", icon="🔐", icon_file=constants.LOCK_ICON, label="Windows Security", query="start windowsdefender:"),
]

STATUS_BAR_LABELS_LEFT = [
    dict(icon="☀ ", icon_file=constants.HIGH_BRIGHTNESS_ICON, text="{}"),
    dict(icon="⚡ ", icon_file=constants.ZAP_ICON, text="{}%"),
    dict(icon="🧠 ", icon_file=constants.BRAIN_ICON, text="{}/{}GB ({}%)"),
    dict(icon="💾 ", icon_file=constants.FLOPPY_DISK_ICON, text="{}/{}TB ({}%)"),
]

STATUS_BAR_LABELS_RIGHT = [
    dict(icon="🔋 ", icon_file=constants.BATTERY_ICON, text="{}%"),
    dict(icon="⌚ ", icon_file=constants.CLOCK_ICON, text="Uptime: {}"),
]

STATUS_BAR_ACTIONS = [
    dict(event="start_app", icon="⚙", icon_file=constants.GEAR_ICON, label="System Settings", query="start ms-settings:"),
    dict(event="start_app", icon="🗨", icon_file=constants.MESSAGES_ICON, label="Action Center", query="start ms-actioncenter:"),
    dict(event="start_app", icon="📶", icon_file=constants.NETWORK_ICON, label="Available Networks", query="start ms-availablenetworks:"),
    dict(event="start_app", icon="🖥", icon_file=constants.DISPLAY_ICON, label="Device Discovery", query="start ms-settings-connectabledevices:devicediscovery"),
]

ACTION_CENTRE_ACTIONS = {
    "Utilities": [
        [
            dict(event="open_url", label="Web\nUtilities", query="www.123apps.com"),
            dict(event="open_url", label="Cloud File\nConverter", query="www.cloudconvert.com"),
            dict(event="open_url", label="Digital\nPDF Tools", query="www.smallpdf.com/pdf-tools"),
            dict(event="open_url", label="Online\nPhoto Editor", query="www.photopea.com"),
            dict(event="open_url", label="Net\nSpeed", query="www.speedtest.net"),
        ],
        [
            dict(event="open_url", label="Bored\nButton", query="www.boredbutton.com/random"),
            dict(event="open_url", label="Wikipedia", query="www.wikipedia.org"),
            dict(event="open_url", label="Library\nGenesis", query="libgen.rs/index.php"),
            dict(event="open_url", label="Good\nReads", query="www.readsomethinggreat.com"),
            dict(event="open_url", label="Drive &\nListen", query="https://driveandlisten.herokuapp.com/"),
        ],
    ],
    "System Apps": [
        [
            dict(event="start_app", label="System\nInformation", query="start msinfo32"),
            dict(event="start_app", label="Task\nManager", query="start taskmgr"),
            dict(event="start_app", label="Performance\nMonitor", query="start perfmon"),
            dict(event="start_app", label="Device\nManagement", query="start devmgmt"),
            dict(event="start_app", label="Disk\nManagement", query="start diskmgmt"),
        ],
        [
            dict(event="start_app", label="Installed\nApps", query="start explorer.exe Shell:::AppsFolder"),
            dict(event="start_app", label="Root\nFolder", query="start explorer.exe Shell:::{59031a47-3f72-44a7-89c5-5595fe6b30ee}"),
            dict(event="start_app", label="Run", query="start explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"),
            dict(event="start_app", label="Control\nPanel", query="start control"),
            dict(event="start_app", label="Registry\nEditor", query="start regedit"),
        ],
    ],
    "Health Check": [
        [
            dict(event="execute_subprocess", label="Echo System\nInformation", query="systeminfo"),
            dict(event="execute_subprocess", label="Running\nApps", query="net start"),
            dict(event="execute_subprocess", label="Running\nProcesses", query="tasklist"),
            dict(event="execute_subprocess", label="Environment\nVariables", query="set"),
            dict(event="execute_subprocess", label="Available\nDrivers", query="driverquery"),
        ],
        [
            dict(event="execute_subprocess", label="Ping", query="ping 8.8.8.8"),
            dict(event="execute_subprocess", label="List DNS\nServers", query="ipconfig /displaydns"),
            dict(event="execute_subprocess", label="Initiate\nDNS Flush", query="ipconfig /flushdns"),
            dict(event="execute_subprocess", label="Network\nConnections", query="netstat -an"),
            dict(event="execute_subprocess", label="IP\nConfigurations", query="ipconfig /allcompartments /all"),
        ],
        [
            dict(event="execute_subprocess", label="Address\nResolution\nProtocol", query="arp -a"),
            dict(event="execute_subprocess", label="File Type\nAssociation", query="ftype"),
            dict(event="execute_subprocess", label="Local Routing\nTable", query="route print"),
            dict(event="execute_subprocess", label="List MAC\nAddresses", query="getmac"),
            dict(event="start_app", label="God\nMode", query="start explorer.exe Shell:::{ED7BA470-8E54-465E-825C-99712043E01C}"),
        ],
    ],
}

MENUS = {
    "Socials": [
        dict(event="open_url", label="Facebook", query="www.facebook.com"),
        dict(event="open_url", label="Instagram", query="www.instagram.com"),
        dict(event="open_url", label="Reddit", query="www.reddit.com"),
        dict(event="open_url", label="Twitter", query="www.twitter.com"),
        "---",
        dict(event="open_url", label="Telegram", query="web.telegram.org"),
        dict(event="open_url", label="Whatsapp", query="web.whatsapp.com"),
        dict(event="open_url", label="Discord", query="www.discord.com/app"),
        dict(event="open_url", label="Slack", query="www.slack.com"),
        "---",
        dict(event="open_url", label="Tumblr", query="www.tumblr.com"),
        dict(event="open_url", label="Pinterest", query="www.pinterest.com"),
        dict(event="open_url", label="Linkedin", query="www.linkedin.com"),
    ]
}

CHATBOT_ACTIONS = [
    dict(event="nicole_respond", icon_file=constants.ARROW_FORWARD_ICON, label="Send Message (Enter)"),
    dict(event="nicole_clear", icon_file=constants.X_ICON, label="Clear Contents"),
]

IEXE_ACTIONS = [
    dict(icon="🔎", icon_file=constants.MAG_RIGHT_ICON, label="Search Online", event="search_query"),
    dict(icon="▶", icon_file=constants.ARROW_FORWARD_ICON, label="Execute Command", event="execute_cmd"),
    dict(icon="📖", icon_file=constants.BOOK_ICON, label="Wiki Article", event="fetch_wiki"),
]

"""
Local Time Zone - tzutil /g
"""

"""Deprecated Actions"""

# dict(event="start_app", label="Command\nPrompt", query="start cmd /k cd /d %USERPROFILE%\Desktop"),