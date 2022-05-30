"""Applications & Commands used in afterlife"""

NATIVE_APPS = {
    "System Settings": [
        dict(event="start", label="Settings", query="start ms-settings:"),
        dict(event="start", label="Action Center", query="start ms-actioncenter:"),
        dict(event="start", label="Available Networks", query="start ms-availablenetworks:"),
        dict(event="start", label="Device Discovery", query="start ms-settings-connectabledevices:devicediscovery"),
    ],
    "Most Used": [
        dict(event="start", label="Alarms & Clock", query="start ms-clock:"),
        dict(event="start", label="Calculator", query="start calculator:"),
        dict(event="start", label="Calendar", query="start outlook cal:"),
        dict(event="start", label="Camera", query="start microsoft.windows.camera:"),
        dict(event="start", label="Drawboard PDF", query="start drawboardpdf:"),
        dict(event="start", label="Groove Music", query="start mswindowsmusic:"),
        dict(event="start", label="Mail", query="start outlookmail:"),
        dict(event="start", label="Microsoft Edge", query="start microsoft-edge:"),
        dict(event="start", label="Microsoft Whiteboard", query="start ms-whiteboard-cmd:"),
        dict(event="start", label="Movies & TV", query="start mswindowsvideo:"),
        dict(event="start", label="Photos", query="start ms-photos:"),
        dict(event="start", label="Screen Snip", query="start ms-screenclip:"),
        dict(event="start", label="Snip & Sketch", query="start ms-ScreenSketch:"),
        dict(event="start", label="Windows Security", query="start windowsdefender:"),
    ],
    "Least Used": [
        dict(event="start", label="3D Builder", query="start com.microsoft.builder3d:"),
        dict(event="start", label="3D Viewer", query="start com.microsoft.3dviewer:"),
        dict(event="start", label="Cortana", query="start ms-cortana:"),
        dict(event="start", label="Feedback Hub", query="start feedback-hub:"),
        dict(event="start", label="Get Help", query="start ms-contact-support:"),
        dict(event="start", label="Maps", query="start bingmaps:"),
        dict(event="start", label="Messaging", query="start ms-chat:"),
        dict(event="start", label="Microsoft News", query="start bingnews:"),
        dict(event="start", label="Microsoft Store", query="start ms-windows-store:"),
        dict(event="start", label="Paint 3D", query="start ms-paint:"),
        dict(event="start", label="People", query="start ms-people:"),
        dict(event="start", label="Tips", query="start ms-get-started:"),
        dict(event="start", label="Weather", query="start bingweather:"),
        dict(event="start", label="Xbox", query="start xbox:"),
    ]
}

ACTIONS = {
    0: [
        dict(event="start", label="Installed\nApps", query="start explorer.exe Shell:::AppsFolder"),
        dict(event="start", label="Root\nFolder", query="start explorer.exe Shell:::{59031a47-3f72-44a7-89c5-5595fe6b30ee}"),
        dict(event="start", label="Task\nManager", query="start taskmgr"),
        dict(event="start", label="Control\nPanel", query="start control"),
        dict(event="start", label="System\nSettings", query="start ms-settings:"),
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
        dict(event="start", label="Notepad", query="start notepad"),
        dict(event="start", label="Sticky Notes", query="start explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App"),
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
        dict(event="start", label="Command Prompt", query="start cmd /k cd /d %USERPROFILE%\Desktop"),
        dict(event="start", label="query Prompt - Admin", query='start powershell "start cmd -v runAs"'),
        dict(event="start", label="Powershell", query="start powershell"),
        dict(event="start", label="WSL Bash", query="start bash"),
        "---",
        dict(event="start", label="Python", query="start python"),
        dict(event="start", label="Node", query="start node"),
    ],
    "Network": [
        dict(event="subprocess", label="Ping", query="ping www.google.com"),
        "---",
        dict(event="subprocess", label="List DNS Servers", query="ipconfig /displaydns"),
        dict(event="subprocess", label="Initiate DNS Flush", query="ipconfig /flushdns"),
        "---",
        dict(event="subprocess", label="Network Connections", query="netstat -an"),
        dict(event="subprocess", label="IP Configurations", query="ipconfig /allcompartments /all"),
    ],
    "Advanced": [
        dict(event="subprocess", label="System Info", query="systeminfo"),
        dict(event="subprocess", label="Running Processes", query="tasklist"),
        dict(event="subprocess", label="Environment Variables", query="set"),
        dict(event="subprocess", label="Available Drivers", query="driverquery"),
        "---",
        dict(event="start", label="Installed Apps", query="start cmd /k wmic product get name,version"),
        "---",
        dict(event="start", label="Run", query="start explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"),
        dict(event="start", label="God Mode", query="start explorer.exe Shell:::{ED7BA470-8E54-465E-825C-99712043E01C}"),
        dict(event="start", label="Device Management", query="start devmgmt"),
        dict(event="start", label="Disk Management", query="start diskmgmt"),
        dict(event="start", label="Registry Editor", query="start regedit"),
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
