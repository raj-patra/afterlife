"""Call to actions used in afterlife"""

from application.helpers import constants

STATUS_BAR_STATS = [
    dict(icon="☀ ", icon_file=constants.HIGH_BRIGHTNESS_ICON, text="{}"),
    dict(icon="🔋", icon_file=constants.BATTERY_ICON, text="{}%"),
    dict(icon="💾 ", icon_file=constants.FLOPPY_DISK_ICON, text="{}/{}TB ({}%)"),
    dict(icon="🖥️", icon_file=constants.BRAIN_ICON, text="{}/{}GB ({}%)"),
    dict(icon="⚡", icon_file=constants.ZAP_ICON, text="{}%"),
]

ACTION_CENTRE_ACTIONS = {
    "Windows apps": [
        [
            dict(event="open_app", label="🤖 Microsoft\nCopilot", query="start ms-copilot:"),
            dict(event="open_app", label="🌐 Microsoft\nEdge", query="start microsoft-edge:"),
            dict(event="open_app", label="➗ Calculator", query="start calculator:"),
            dict(event="open_app", label="📆 Calendar", query="start outlook cal:"),
            dict(event="open_app", label="📸 Camera", query="start microsoft.windows.camera:"),
        ],
        [
            dict(event="open_app", label="⏰ Alarms & Clock", query="start ms-clock:"),
            dict(event="open_app", label="📧 Mail", query="start outlookmail:"),
            dict(event="open_app", label="🗺 Maps", query="start bingmaps:"),
            dict(event="open_app", label="🎥 Movies & TV", query="start mswindowsvideo:"),
            dict(event="open_app", label="🎶 Groove Music", query="start mswindowsmusic:"),
        ],
        [
            dict(event="open_app", label="🤳 Photos", query="start ms-photos:"),
            dict(event="open_app", label="🎨 Paint", query="start mspaint"),
            dict(event="open_app", label="✂ Snip & Sketch", query="start ms-ScreenSketch:"),
            dict(event="open_app", label="🗒 Notepad", query="start notepad"),
            dict(event="open_app", label="⛅ Weather", query="start bingweather:"),
        ],
        [
            dict(event="open_app", label="🗨 Action\nCenter", query="start ms-actioncenter:"),
            dict(event="open_app", label="📶 Available\nNetworks", query="start ms-availablenetworks:"),
            dict(event="open_app", label="🖥 Device\nDiscovery", query="start ms-settings-connectabledevices:devicediscovery"),
            dict(event="open_app", label="🔐 Windows\nSecurity", query="start windowsdefender:"),
            dict(event="open_app", label="⚙ System\nSettings", query="start ms-settings:"),
        ],
    ],
    "Power user": [
        [
            dict(event="open_app", label="Task\nManager", query="start taskmgr"),
            dict(event="open_app", label="Reliability\nMonitor", query="perfmon /rel"),
            dict(event="open_app", label="Performance\nMonitor", query="start perfmon"),
            dict(event="open_app", label="Device\nManagement", query="start devmgmt"),
            dict(event="open_app", label="Disk\nManagement", query="start diskmgmt"),
        ],
        [
            dict(event="open_app", label="User\nFolder", query="start explorer.exe Shell:::{59031a47-3f72-44a7-89c5-5595fe6b30ee}"),
            dict(event="open_app", label="Control\nPanel", query="start control"),
            dict(event="open_app", label="Run", query="start explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"),
            dict(event="open_app", label="System\nInformation", query="start msinfo32"),
            dict(event="open_app", label="Registry\nEditor", query="start regedit"),
        ],
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
            dict(event="execute_subprocess", label="Local Routing\nTable", query="route print"),
            dict(event="execute_subprocess", label="List MAC\nAddresses", query="getmac"),
            dict(event="execute_subprocess", label="File Type\nAssociation", query="ftype"),
            dict(event="open_app", label="God\nMode", query="start explorer.exe Shell:::{ED7BA470-8E54-465E-825C-99712043E01C}"),
        ],
    ],
}

MENUS = {
    "Web Utilities": [
        dict(event="open_url", label="Web Utilities", query="www.123apps.com"),
        dict(event="open_url", label="Cloud File Converter", query="www.cloudconvert.com"),
        dict(event="open_url", label="Digital PDF Tools", query="www.smallpdf.com/pdf-tools"),
        dict(event="open_url", label="Online Photo Editor", query="www.photopea.com"),
        dict(event="open_url", label="Net Speed", query="www.speedtest.net"),
    ],
    "Study": [
        dict(event="open_url", label="Wikipedia", query="www.wikipedia.org"),
        dict(event="open_url", label="Library Genesis", query="libgen.rs/index.php"),
        dict(event="open_url", label="Good Reads", query="www.readsomethinggreat.com"),
    ],
    "Recreation": [
        dict(event="open_url", label="Slowroads", query="https://slowroads.io/"),
        dict(event="open_url", label="Bored Button", query="www.boredbutton.com/random"),
        dict(event="open_url", label="Drive & Listen", query="https://driveandlisten.herokuapp.com/"),
    ],
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
    ],
    
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

# dict(event="open_app", label="Command\nPrompt", query="start cmd /k cd /d %USERPROFILE%\Desktop"),