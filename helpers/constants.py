import random, requests, getmac, socket
import subprocess as sp

BUTTONS = {

    0: [['All Apps', 'start explorer.exe Shell:::{4234d49b-0245-4df3-b780-3893943456e1}'], 
        ["Root\nFolder", "start explorer.exe Shell:::{59031a47-3f72-44a7-89c5-5595fe6b30ee}"],
        ["Task\nManager", "start taskmgr"], ["Control\nPanel", "start control"],
        ["Run", "start explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"]],

    1: [['Google', 'google.com'], ['Gmail', 'mail.google.com'], ['Youtube', 'youtube.com'], 
        ['Maps', 'maps.google.com'], ['Keep', 'keep.google.com']],

    2: [['Docs', 'docs.new'], ['Sheets', 'sheets.new'], ['Slides', 'slides.new'], ["Notepad", "start notepad"], 
        ["Sticky Notes", "start explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App"]],

    3: [['Instagram', 'instagram.com'], ['Reddit', 'reddit.com'], ['Twitter', 'twitter.com'], 
        ['Telegram', 'web.telegram.org'], ['Whatsapp', 'web.whatsapp.com']],

    4: [['Spotify', 'open.spotify.com'], ['Tumblr', 'tumblr.com'], ['Linkedin', 'linkedin.com'], 
        ['Pinterest', 'pinterest.com'], ['Facebook', "facebook.com"]],

    5: [['Cloud\nConvert', 'cloudconvert.com'], ['PDF\nTools', 'smallpdf.com/pdf-tools'], ['Utilities', '123apps.com'],  
        ['Net\nSpeed', 'openspeedtest.com/?ref=OST-Results'], ['Library\nGenesis', "libgen.rs/index.php"]],

}

MENUS = {
    "Native Apps": [ ['Windows Mail', 'start outlookmail:'], 
                ['Calculator', 'start calc'], 
                ['Calendar', 'start outlookcal:'], 
                ['Camera', 'start microsoft.windows.camera:'], 
                ['Groove Music', 'start mswindowsmusic:'], 
                ["MS Paint", "start mspaint"]],

    "CLIs": [   ["Command Prompt ", "start cmd /k cd /d %USERPROFILE%\Desktop"], 
                ["WSL Bash", "start bash"], 
                ["Powershell", " start powershell"], "---",

                ["Python", " start python"],
                ["Node", " start node"]],

    "Network": [["Ping", "subprocess ping google.com"], 
                ["List DNS Servers", "subprocess ipconfig /displaydns"], 
                ["Initiate DNS Flush", "subprocess ipconfig /flushdns"], 
                ["IP Configurations", "subprocess ipconfig /allcompartments /all"]],

    "Advanced": [
                ["God Mode", "start explorer.exe Shell:::{ED7BA470-8E54-465E-825C-99712043E01C}"],
                ["Registry Editor", "start regedit"], 
                ["Disk Management", "start diskmgmt"], "---",
                
                ["System Info", "subprocess systeminfo"], 
                ["Running Processes", "subprocess tasklist"], 
                ["Environment Variables", "subprocess set"], 
                ["Available Drivers", "subprocess driverquery"]],

    "Socials":  [['Facebook', "facebook.com"], ['Instagram', 'instagram.com'], ['Reddit', 'reddit.com'], ['Twitter', 'twitter.com'], "---",
                ['Telegram', 'web.telegram.org'], ['Whatsapp', 'web.whatsapp.com'], "---",
                ['Tumblr', 'tumblr.com'], ['Pinterest', 'pinterest.com'], ['Linkedin', 'linkedin.com']],
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

QUOTE_API = "https://api.quotable.io/random"

PUB_IP = requests.get('https://ident.me').text
PRI_IP = socket.gethostbyname(socket.gethostname())
MAC = getmac.get_mac_address()
HOST = sp.getoutput("hostname")
USER = sp.getoutput("whoami")

DISK = sp.getoutput("wmic logicaldisk get size,freespace,caption").replace("\n\n", "\n")

WELCOME = """
Hey there, {}
I hope you are having a good day.
.
.
Just remember, wherever you go, leave your mark behind.
Have fun.""".format('-'.join([random.choice(ADJECTIVES), random.choice(NOUNS)]))

SYSTEM = """
CPU Usage: {} %
Memory: {} %

{}: {:.1f} %
Battery: {} % {}

------------------------------------

"""+DISK

NETWORK = """
Host Name: {}

User: {}

Public IP: {}

Private IP: {}

MAC Address: {}

Default Gateway: 192.168.0.0/1
""".format(HOST, USER, PUB_IP, PRI_IP, MAC)

ABOUT = """
Afterlife is a minimalistic HUD.

It brings all the important functions/commands of Windows to the fingertips of its users and helps them connect to the internet faster.

Made with ♥ by a_ignorant_mortal
""".strip()