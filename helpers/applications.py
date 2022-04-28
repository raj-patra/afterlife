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
