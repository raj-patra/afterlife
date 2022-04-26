import random, requests, getmac, socket
from tkinter.constants import CURRENT
import subprocess as sp

BUTTONS = {

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

    5: [['Daily\nQuote', 'request quote'], ['Did you\nknow?', 'request fact'], ['A Poem?', 'request poem'],
        ['Kanye\nREST', 'request kanye'], ['Rare\nInsult', 'request insult']],

}

MENUS = {
    "CLIs": [
        ["Command Prompt ", "start cmd /k cd /d %USERPROFILE%\Desktop"],
        ["Command Prompt - Admin", 'start powershell "start cmd -v runAs"'],
        ["Powershell", " start powershell"],
        ["WSL Bash", "start bash"], "---",

        ["Python", " start python"],
        ["Node", " start node"]
    ],
    "Network": [
        ["Ping", "subprocess ping www.google.com"], "---",
        ["List DNS Servers", "subprocess ipconfig /displaydns"],
        ["Initiate DNS Flush", "subprocess ipconfig /flushdns"], "---",
        ["Network Connections", "subprocess netstat -an"],
        ["IP Configurations", "subprocess ipconfig /allcompartments /all"]
    ],
    "Advanced": [
        ["System Info", "subprocess systeminfo"],
        ["Running Processes", "subprocess tasklist"],
        ["Environment Variables", "subprocess set"],
        ["Available Drivers", "subprocess driverquery"], "---",

        ["Installed Apps", "start cmd /k wmic product get name,version"], "---",

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

NOUNS = [
    'fishbowl', 'chairman', 'vineyard', 'caretaker', 'carwash', 'inland', 'barnyard', 'because', 'password', 'fireman', 'worldwide', 'buttercup', 'quicksand', 'courthouse', 'workshop', 'dustpan', 'backfield', 'bobcat', 'ratline', 'background', 'bathroom', 'rawboned', 'grapefruit', 'aircraft', 'talebearer',
    'tapeworm', 'crackpot', 'rattlesnake', 'courtroom', 'rearward', 'teaspoon', 'became', 'countermeasure', 'passbook', 'earthworm', 'countdown', 'copycat', 'lifetime', 'cartwheel', 'stonewall', 'checkmate', 'carport', 'bedbug', 'airfield', 'passkey', 'taleteller', 'candid', 'ladybug', 'stepson', 'bedclothes',
    'outdoors', 'drawstring', 'cutthroat', 'rawhide', 'armchair', 'hallway', 'crossbeam', 'lifeblood', 'lifeboat', 'darkroomṇ', 'caveman', 'counterpoise', 'redcoat', 'earache', 'baseball', 'gateway', 'rearmost', 'reddish', 'oatmeal', 'jigsaw', 'fourteen', 'standpipe', 'carefree', 'earring', 'mealtime', 'eyebrow',
    'earphone', 'chopstick', 'courtyard', 'stickup', 'yourself', 'flashback', 'cardsharp', 'pancake', 'greenhouse', 'kneecap', 'keyhole', 'seashell', 'backfire', 'dishwasher', 'ratsbane', 'starfish', 'crybaby', 'firefly', 'lifesaver', 'drawbridge', 'readywitted', 'eggplant', 'handgun', 'eyeball', 'candlelight', 'notebook',
    'household', 'lifework', 'steamship', 'airbrush', 'raincoat', 'cheesecloth', 'heartbeat', 'carrack', 'rattletrap', 'backbreaker', 'elsewhere', 'eyelid', 'darkroom', 'carpool', 'railway', 'carsick', 'handcuff', 'cancan', 'crybaby', 'grasshopper', 'together', 'rainbow', 'armpit', 'backlash', 'iceberg', 'airlift',
    'eardrum', 'waistline', 'bulldog', 'aftermath', 'nightmare', 'catfish', 'drainpipe', 'briefcase', 'butterfly', 'carryall', 'rainwater', 'Cannot', 'afternoon', 'candlestick', 'teardrop', 'scarecrow', 'cattail', 'rearrange', 'firefly', 'undermine', 'become', 'bedtime', 'wallpaper', 'clockwork', 'carpetbagger',
    'earthquake', 'stockroom', 'driveway', 'footprint', 'backdrop', 'drumstick', 'counteroffensive', 'daredevil', 'cardboard', 'landslide', 'billboard', 'foolproof', 'marketplace', 'steamboat', 'endless', 'breakfast', 'sailboat', 'driftwood', 'cowboy', 'daydream', 'Passover', 'redcap', 'brainstorm']

ADJECTIVES = [
    'adorable', 'adventurous', 'aggressive', 'agreeable', 'alert', 'alive', 'amused', 'angry', 'calm', 'careful', 'cautious', 'charming', 'cheerful', 'clean', 'clear', 'clever', 'cloudy', 'clumsy', 'eager', 'easy', 'elated', 'elegant', 'embarrassed', 'enchanting', 'encouraging', 'bad', 'beautiful', 'better',
    'bewildered', 'black', 'bloody', 'blue', 'blue-eyed', 'dangerous', 'dark', 'dead', 'defeated', 'defiant', 'delightful', 'depressed', 'determined', 'different', 'fair', 'faithful', 'famous', 'fancy', 'fantastic', 'fierce', 'filthy', 'fine', 'annoyed', 'annoying', 'anxious', 'arrogant', 'ashamed', 'attractive',
    'average', 'awful', 'colorful', 'combative', 'comfortable', 'concerned', 'condemned', 'confused', 'cooperative', 'courageous', 'curious', 'cute', 'energetic', 'enthusiastic', 'envious', 'evil', 'excited', 'expensive', 'exuberant', 'blushing', 'bored', 'brainy', 'brave', 'breakable', 'bright', 'busy', 'buttery',
    'difficult', 'disgusted', 'distinct', 'disturbed', 'dizzy', 'doubtful', 'drab', 'dull', 'dusty', 'foolish', 'fragile', 'frail', 'frantic', 'friendly', 'frightened', 'funny', 'furry', 'gentle', 'gifted', 'glamorous', 'gleaming', 'glorious', 'good', 'ill', 'important', 'impossible', 'inexpensive', 'innocent',
    'inquisitive', 'nasty', 'naughty', 'nervous', 'nice', 'nutty', 'obedient', 'obnoxious', 'odd', 'old-fashioned', 'handsome', 'happy', 'healthy', 'helpful', 'helpless', 'hilarious', 'lazy', 'light', 'lively', 'lonely', 'long', 'lovely', 'lucky', 'panicky', 'perfect', 'plain', 'pleasant', 'poised', 'poor', 'powerful',
    'gorgeous', 'graceful', 'grieving', 'grotesque', 'grumpy', 'grungy', 'itchy', 'jealous', 'jittery', 'jolly', 'joyous', 'kind', 'open', 'outrageous', 'outstanding', 'homeless', 'homely', 'horrible', 'hungry', 'hurt', 'hushed', 'magnificent', 'misty', 'modern', 'motionless', 'muddy', 'mushy', 'mysterious', 'precious',
    'prickly', 'proud', 'putrid', 'puzzled', 'quaint', 'queasy', 'real', 'relieved', 'repulsive', 'rich', 'scary', 'selfish', 'shiny', 'shy', 'silly', 'sleepy', 'smiling', 'vast', 'victorious', 'vivacious', 'wandering', 'weary', 'wicked', 'wide-eyed', 'talented', 'tame', 'tasty', 'tender', 'tense', 'terrible', 'thankful',
    'thoughtful', 'thoughtless', 'tired', 'smoggy', 'sore', 'sparkling', 'splendid', 'spotless', 'stormy', 'strange', 'stupid', 'successful', 'super ', 'svelte', 'wild', 'witty', 'worried', 'worrisome', 'wrong', 'zany', 'zealous', 'tough', 'troubled', 'ugliest', 'ugly', 'uninterested', 'unsightly', 'unusual', 'upset',
    'uptight', 'useful']

# ----------------------------------------------------------------------------------

QUOTE_API = "https://api.quotable.io/random"
INSULT_API = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
FACTS_API = "https://uselessfacts.jsph.pl//random.json?language=en"
POEMS_API = "https://www.poemist.com/api/v1/randompoems"
KANYE_API = "https://api.kanye.rest/"

# ----------------------------------------------------------------------------------

try:
    PUB_IP = requests.get('https://ident.me').text
except Exception as e:
    PUB_IP = "NA. Error Occured."

PRI_IP = socket.gethostbyname(socket.gethostname())
MAC = getmac.get_mac_address()
HOST = sp.getoutput("hostname")
USER = sp.getoutput("whoami")

boot = sp.getoutput("wmic path Win32_OperatingSystem get LastBootUpTime").split('\n')[2].split('.')[0]
LAST_BOOT = "Last Bootup Time: {}{}/{}/{} {}:{}:{}".format(*[boot[i:i+2] for i in range(0, len(boot), 2)])
DISK = sp.getoutput("wmic logicaldisk get size,freespace,caption").replace("\n\n", "\n")

# ----------------------------------------------------------------------------------

WELCOME = """
Hey there, {}
I hope you are having a good day.

Just remember, wherever you go, leave your mark behind.
Have fun.

""".format('-'.join([random.choice(ADJECTIVES), random.choice(NOUNS)]))

CURRENT_THEME = "FYI, Current theme: {}"

# ----------------------------------------------------------------------------------

SYSTEM = '\n'+LAST_BOOT+'\n\n'+DISK+"""CPU Usage: {}%   |   RAM Usage: {}%

{}: {:.1f} %

Battery: {}% {}"""

# ----------------------------------------------------------------------------------

NETWORK = """
Host: {}

User: {}

Public IP: {}

Private IP: {}

MAC Address: {}
""".format(HOST, USER, PUB_IP, PRI_IP, MAC)

# ----------------------------------------------------------------------------------

ABOUT = """
Afterlife is a minimalistic HUD.

It brings all the important functions/commands of Windows to the fingertips of its users. It also highlights some of the popular internet services/utilities.

Made with ♥ by a_ignorant_mortal
""".strip()

# ----------------------------------------------------------------------------------

WIKI = """
Title - {}
Details at - {}

Summary - {}
"""
