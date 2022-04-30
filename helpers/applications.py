"""Applications used in afterlife"""

NATIVE_APPS = {
    "System Settings": [
        dict(name="Settings", command="start ms-settings:"),
        dict(name="Action Center", command="start ms-actioncenter:"),
        dict(name="Available Networks", command="start ms-availablenetworks:"),
        dict(name="Device Discovery", command="start ms-settings-connectabledevices:devicediscovery"),
    ],
    "Most Used": [
        dict(name="Alarms & Clock", command="start ms-clock:"),
        dict(name="Calculator", command="start calculator:"),
        dict(name="Calendar", command="start outlook cal:"),
        dict(name="Camera", command="start microsoft.windows.camera:"),
        dict(name="Drawboard PDF", command="start drawboardpdf:"),
        dict(name="Groove Music", command="start mswindowsmusic:"),
        dict(name="Mail", command="start outlookmail:"),
        dict(name="Microsoft Edge", command="start microsoft-edge:"),
        dict(name="Microsoft Whiteboard", command="start ms-whiteboard-cmd:"),
        dict(name="Movies & TV", command="start mswindowsvideo:"),
        dict(name="Photos", command="start ms-photos:"),
        dict(name="Screen Snip", command="start ms-screenclip:"),
        dict(name="Snip & Sketch", command="start ms-ScreenSketch:"),
        dict(name="Windows Security", command="start windowsdefender:"),
    ],
    "Least Used": [
        dict(name="3D Builder", command="start com.microsoft.builder3d:"),
        dict(name="3D Viewer", command="start com.microsoft.3dviewer:"),
        dict(name="Cortana", command="start ms-cortana:"),
        dict(name="Feedback Hub", command="start feedback-hub:"),
        dict(name="Get Help", command="start ms-contact-support:"),
        dict(name="Maps", command="start bingmaps:"),
        dict(name="Messaging", command="start ms-chat:"),
        dict(name="Microsoft News", command="start bingnews:"),
        dict(name="Microsoft Store", command="start ms-windows-store:"),
        dict(name="Paint 3D", command="start ms-paint:"),
        dict(name="People", command="start ms-people:"),
        dict(name="Tips", command="start ms-get-started:"),
        dict(name="Weather", command="start bingweather:"),
        dict(name="Xbox", command="start xbox:"),
    ]
}

ACTION_CENTRE = {

    0: [['All\nApps', 'start explorer.exe Shell:::AppsFolder'],
        ["Root\nFolder", "start explorer.exe Shell:::{59031a47-3f72-44a7-89c5-5595fe6b30ee}"],
        ["Task\nManager", "start taskmgr"], ["Control\nPanel", "start control"],
        ['System\nSettings', 'start ms-settings:'],
        ],

    1: [['Google', 'url www.google.com'], ['Gmail', 'url mail.google.com'], ['Youtube', 'url www.youtube.com'],
        ['Maps', 'url maps.google.com'], ['Keep', 'url keep.google.com']],

    2: [['Docs', 'url docs.new'], ['Sheets', 'url sheets.new'], ['Slides', 'url slides.new'], ["Notepad", "start notepad"],
        ["Sticky Notes", "start explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App"]],

    3: [['Cloud\nConvert', 'url www.cloudconvert.com'], ['PDF\nTools', 'url www.smallpdf.com/pdf-tools'], ['Utilities', 'url www.123apps.com'],
        ['Net\nSpeed', 'url www.speedtest.net'], ['Photopea\nEditor', "url www.photopea.com"]],

    4: [['Spotify', 'url open.spotify.com'], ['Bored\nButton', 'url www.boredbutton.com/random'], ['Wikipedia', 'url www.wikipedia.org'],
        ['Library\nGenesis', "url libgen.rs/index.php"], ['Good Reads', 'url www.readsomethinggreat.com']],

}

MENUS = {
    "CLIs": [
        ["Command Prompt ", "start cmd /k cd /d %USERPROFILE%\Desktop"],
        ["Command Prompt - Admin", 'start powershell "start cmd -v runAs"'],
        ["Powershell", " start powershell"],
        ["WSL Bash", "start bash"],
        "---",
        ["Python", " start python"],
        ["Node", " start node"]
    ],
    "Network": [
        ["Ping", "subprocess ping www.google.com"],
        "---",
        ["List DNS Servers", "subprocess ipconfig /displaydns"],
        ["Initiate DNS Flush", "subprocess ipconfig /flushdns"],
        "---",
        ["Network Connections", "subprocess netstat -an"],
        ["IP Configurations", "subprocess ipconfig /allcompartments /all"]
    ],
    "Advanced": [
        ["System Info", "subprocess systeminfo"],
        ["Running Processes", "subprocess tasklist"],
        ["Environment Variables", "subprocess set"],
        ["Available Drivers", "subprocess driverquery"],
        "---",
        ["Installed Apps", "start cmd /k wmic product get name,version"],
        "---",
        ["Run", "start explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"],
        ["God Mode", "start explorer.exe Shell:::{ED7BA470-8E54-465E-825C-99712043E01C}"],
        ["Device Management", "start devmgmt"], ["Disk Management", "start diskmgmt"],
        ["Registry Editor", "start regedit"]
    ],
    "Socials": [
        ['Facebook', "url www.facebook.com"], ['Instagram', 'url www.instagram.com'], ['Reddit', 'url www.reddit.com'], ['Twitter', 'url www.twitter.com'], "---",
        ['Telegram', 'url web.telegram.org'], ['Whatsapp', 'url web.whatsapp.com'], ["Discord", "www.discord.com/app"], ["Slack", "url www.slack.com"], "---",
        ['Tumblr', 'url www.tumblr.com'], ['Pinterest', 'url www.pinterest.com'], ['Linkedin', 'url www.linkedin.com']
    ],
}
