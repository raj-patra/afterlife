"""Call to actions used in afterlife"""

SIDE_BAR_ACTIONS = [
    dict(event="start_app", icon="⏰", icon_file="./assets/icons/google/clock.png",
        label="Alarms & Clock", query="start ms-clock:"),
    dict(event="start_app", icon="➗", icon_file="./assets/icons/google/division.png",
        label="Calculator", query="start calculator:"),
    dict(event="start_app", icon="📆", icon_file="./assets/icons/google/calendar.png",
        label="Calendar", query="start outlook cal:"),
    dict(event="start_app", icon="📸", icon_file="./assets/icons/google/camera.png",
        label="Camera", query="start microsoft.windows.camera:"),
    dict(event="start_app", icon="🤖", icon_file="./assets/icons/google/robot.png",
        label="Cortana", query="start ms-cortana:"),
    dict(event="start_app", icon="🎶", icon_file="./assets/icons/google/music.png",
        label="Groove Music", query="start mswindowsmusic:"),
    dict(event="start_app", icon="📧", icon_file="./assets/icons/google/email.png",
        label="Mail", query="start outlookmail:"),
    dict(event="start_app", icon="🗺", icon_file="./assets/icons/google/maps.png",
        label="Maps", query="start bingmaps:"),
    dict(event="start_app", icon="🌐", icon_file="./assets/icons/google/internet.png",
        label="Microsoft Edge", query="start microsoft-edge:"),
    dict(event="start_app", icon="🎥", icon_file="./assets/icons/google/video.png",
        label="Movies & TV", query="start mswindowsvideo:"),
    dict(event="start_app", icon="🎨", icon_file="./assets/icons/google/art.png",
        label="Paint 3D", query="start ms-paint:"),
    dict(event="start_app", icon="🤳", icon_file="./assets/icons/google/selfie.png",
        label="Photos", query="start ms-photos:"),
    dict(event="start_app", icon="✂", icon_file="./assets/icons/google/scissors.png",
        label="Snip & Sketch", query="start ms-ScreenSketch:"),
    dict(event="start_app", icon="⛅", icon_file="./assets/icons/google/weather.png",
        label="Weather", query="start bingweather:"),
    dict(event="start_app", icon="🔐", icon_file="./assets/icons/google/lock.png",
        label="Windows Security", query="start windowsdefender:"),
]

STATUS_BAR_LABELS_LEFT = [
    dict(icon="☀ ", icon_file="./assets/icons/google/high_brightness.png", text="{}"),
    dict(icon="⚡ ", icon_file="./assets/icons/google/zap.png", text="{}%"),
    dict(icon="🧠 ", icon_file="./assets/icons/google/brain.png", text="{}/{}GB ({}%)"),
    dict(icon="💾 ", icon_file="./assets/icons/google/floppy_disk.png", text="{}/{}TB ({}%)"),
]

STATUS_BAR_LABELS_RIGHT = [
    dict(icon="🔋 ", icon_file="./assets/icons/google/battery.png", text="{}%"),
    dict(icon="⌚ ", icon_file="./assets/icons/google/clock.png", text="Uptime: {}"),
]

STATUS_BAR_ACTIONS = [
    dict(event="start_app", icon="⚙", icon_file="./assets/icons/google/gear.png", 
        label="System Settings", query="start ms-settings:"),
    dict(event="start_app", icon="🗨", icon_file="./assets/icons/google/messages.png", 
        label="Action Center", query="start ms-actioncenter:"),
    dict(event="start_app", icon="📶", icon_file="./assets/icons/google/network.png", 
        label="Available Networks", query="start ms-availablenetworks:"),
    dict(event="start_app", icon="🖥", icon_file="./assets/icons/google/display.png", 
        label="Device Discovery", query="start ms-settings-connectabledevices:devicediscovery"),
]

ACTION_CENTRE_ACTIONS = {
    "Windows Actions": [
        [
            dict(event="start_app", label="Installed\nApps", query="start explorer.exe Shell:::AppsFolder"),
            dict(event="start_app", label="Root\nFolder", query="start explorer.exe Shell:::{59031a47-3f72-44a7-89c5-5595fe6b30ee}"),
            dict(event="start_app", label="Task\nManager", query="start taskmgr"),
            dict(event="start_app", label="Control\nPanel", query="start control"),
            dict(event="start_app", label="Command\nPrompt", query="start cmd /k cd /d %USERPROFILE%\Desktop"),
        ],
        [
            dict(event="execute_subprocess", label="System\nInfo", query="systeminfo"),
            dict(event="execute_subprocess", label="Running\nProcesses", query="tasklist"),
            dict(event="execute_subprocess", label="Environment\nVariables", query="set"),
            dict(event="execute_subprocess", label="Available\nDrivers", query="driverquery"),
            dict(event="start_app", label="Notepad", query="start notepad"),
        ],
        [
            dict(event="start_app", label="Run", query="start explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"),
            dict(event="start_app", label="God\nMode", query="start explorer.exe Shell:::{ED7BA470-8E54-465E-825C-99712043E01C}"),
            dict(event="start_app", label="Device\nManagement", query="start devmgmt"),
            dict(event="start_app", label="Disk\nManagement", query="start diskmgmt"),
            dict(event="start_app", label="Registry\nEditor", query="start regedit"),
        ],
    ],
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
    ]
}

MENUS = {
    "Network": [
        dict(event="execute_subprocess", label="Ping", query="ping 8.8.8.8"),
        "---",
        dict(event="execute_subprocess", label="List DNS Servers", query="ipconfig /displaydns"),
        dict(event="execute_subprocess", label="Initiate DNS Flush", query="ipconfig /flushdns"),
        "---",
        dict(event="execute_subprocess", label="Network Connections", query="netstat -an"),
        dict(event="execute_subprocess", label="IP Configurations", query="ipconfig /allcompartments /all"),
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
    ]
}

CHATBOT_ACTIONS = [
    dict(event="nicole_respond", icon_file="./assets/icons/google/arrow_forward.png", label="Send Message (Enter)"),
    dict(event="nicole_clear", icon_file="./assets/icons/google/x.png", label="Clear Contents"),
]

IEXE_ACTIONS = [
    dict(icon="🔎", icon_file="./assets/icons/google/mag_right.png", label="Search Online", event="search_query"),
    dict(icon="▶", icon_file="./assets/icons/google/arrow_forward.png", label="Execute Command", event="execute_cmd"),
    dict(icon="📖", icon_file="./assets/icons/google/book.png", label="Wiki Article", event="fetch_wiki"),
]