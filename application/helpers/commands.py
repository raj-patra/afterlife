"""Applications & Commands used in afterlife"""

SIDE_BAR_ACTIONS = [
    dict(event="start_app", icon="⏰", label="Alarms & Clock", query="start ms-clock:"),
    dict(event="start_app", icon="➗", label="Calculator", query="start calculator:"),
    dict(event="start_app", icon="📆", label="Calendar", query="start outlook cal:"),
    dict(event="start_app", icon="📸", label="Camera", query="start microsoft.windows.camera:"),
    dict(event="start_app", icon="🤖", label="Cortana", query="start ms-cortana:"),
    dict(event="start_app", icon="🎶", label="Groove Music", query="start mswindowsmusic:"),
    dict(event="start_app", icon="📧", label="Mail", query="start outlookmail:"),
    dict(event="start_app", icon="🗺", label="Maps", query="start bingmaps:"),
    dict(event="start_app", icon="🌐", label="Microsoft Edge", query="start microsoft-edge:"),
    dict(event="start_app", icon="🎥", label="Movies & TV", query="start mswindowsvideo:"),
    dict(event="start_app", icon="🎨", label="Paint 3D", query="start ms-paint:"),
    dict(event="start_app", icon="🤳", label="Photos", query="start ms-photos:"),
    dict(event="start_app", icon="✂", label="Snip & Sketch", query="start ms-ScreenSketch:"),
    dict(event="start_app", icon="⛅", label="Weather", query="start bingweather:"),
    dict(event="start_app", icon="🔐", label="Windows Security", query="start windowsdefender:"),
]

STATUS_BAR_ACTIONS = [
    dict(event="start_app", icon="⚙", label="System Settings", query="start ms-settings:"),
    dict(event="start_app", icon="🗨", label="Action Center", query="start ms-actioncenter:"),
    dict(event="start_app", icon="📶", label="Available Networks", query="start ms-availablenetworks:"),
    dict(event="start_app", icon="🖥", label="Device Discovery", query="start ms-settings-connectabledevices:devicediscovery"),
]

ACTIONS = {
    0: [
        dict(event="start_app", label="Installed\nApps", query="start explorer.exe Shell:::AppsFolder"),
        dict(event="start_app", label="Root\nFolder", query="start explorer.exe Shell:::{59031a47-3f72-44a7-89c5-5595fe6b30ee}"),
        dict(event="start_app", label="Task\nManager", query="start taskmgr"),
        dict(event="start_app", label="Control\nPanel", query="start control"),
        dict(event="start_app", label="Command\nPrompt", query="start cmd /k cd /d %USERPROFILE%\Desktop"),
    ],
    1: [
        dict(event="open_url", label="Google", query="www.google.com"),
        dict(event="open_url", label="Gmail", query="mail.google.com"),
        dict(event="open_url", label="Youtube", query="www.youtube.com"),
        dict(event="open_url", label="Maps", query="maps.google.com"),
        dict(event="open_url", label="Keep", query="keep.google.com"),
    ],
    2: [
        dict(event="open_url", label="Docs", query="docs.new"),
        dict(event="open_url", label="Sheets", query="sheets.new"),
        dict(event="open_url", label="Slides", query="slides.new"),
        dict(event="start_app", label="Notepad", query="start notepad"),
        dict(event="start_app", label="Sticky Notes", query="start explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App"),
    ],
    3: [
        dict(event="open_url", label="Web\nUtilities", query="www.123apps.com"),
        dict(event="open_url", label="Cloud File\nConverter", query="www.cloudconvert.com"),
        dict(event="open_url", label="Digital PDF\nTools", query="www.smallpdf.com/pdf-tools"),
        dict(event="open_url", label="Online Photo\nEditor", query="www.photopea.com"),
        dict(event="open_url", label="Net\nSpeed", query="www.speedtest.net"),
    ],
    4: [
        dict(event="open_url", label="Spotify", query="open.spotify.com"),
        dict(event="open_url", label="Bored\nButton", query="www.boredbutton.com/random"),
        dict(event="open_url", label="Wikipedia", query="www.wikipedia.org"),
        dict(event="open_url", label="Library\nGenesis", query="libgen.rs/index.php"),
        dict(event="open_url", label="Good Reads", query="www.readsomethinggreat.com"),
    ]
}

MENUS = {
    "CLIs": [
        dict(event="start_app", label="Command Prompt", query="start cmd /k cd /d %USERPROFILE%\Desktop"),
        dict(event="start_app", label="Command Prompt - Admin", query='start powershell "start cmd -v runAs"'),
        dict(event="start_app", label="Powershell", query="start powershell"),
        dict(event="start_app", label="WSL Bash", query="start bash"),
        "---",
        dict(event="start_app", label="Python", query="start python"),
        dict(event="start_app", label="Node", query="start node"),
    ],
    "Network": [
        dict(event="execute_subprocess", label="Ping", query="ping www.google.com"),
        "---",
        dict(event="execute_subprocess", label="List DNS Servers", query="ipconfig /displaydns"),
        dict(event="execute_subprocess", label="Initiate DNS Flush", query="ipconfig /flushdns"),
        "---",
        dict(event="execute_subprocess", label="Network Connections", query="netstat -an"),
        dict(event="execute_subprocess", label="IP Configurations", query="ipconfig /allcompartments /all"),
    ],
    "Advanced": [
        dict(event="execute_subprocess", label="System Info", query="systeminfo"),
        dict(event="execute_subprocess", label="Running Processes", query="tasklist"),
        dict(event="execute_subprocess", label="Environment Variables", query="set"),
        dict(event="execute_subprocess", label="Available Drivers", query="driverquery"),
        "---",
        dict(event="start_app", label="Installed Apps", query="start cmd /k wmic product get name,version"),
        "---",
        dict(event="start_app", label="Run", query="start explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"),
        dict(event="start_app", label="God Mode", query="start explorer.exe Shell:::{ED7BA470-8E54-465E-825C-99712043E01C}"),
        dict(event="start_app", label="Device Management", query="start devmgmt"),
        dict(event="start_app", label="Disk Management", query="start diskmgmt"),
        dict(event="start_app", label="Registry Editor", query="start regedit"),
    ],
    "Socials": [
        dict(event="open_url", label="Facebook", query="www.facebook.com"),
        dict(event="open_url", label="Instagram", query="www.instagram.com"),
        dict(event="open_url", label="Reddit", query="www.reddit.com"),
        dict(event="open_url", label="Twitter", query="www.twitter.com"),
        "---",
        dict(event="open_url", label="Telegram", query="web.telegram.org"),
        dict(event="open_url", label="Whatsapp", query="web.whatsapp.com"),
        dict(event="open_url", label="Discord", query="wwwdiscord.com/app"),
        dict(event="open_url", label="Slack", query="www.slack.com"),
        "---",
        dict(event="open_url", label="Tumblr", query="www.tumblr.com"),
        dict(event="open_url", label="Pinterest", query="www.pinterest.com"),
        dict(event="open_url", label="Linkedin", query="www.linkedin.com"),
    ],
}
