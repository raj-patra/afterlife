import random, requests, getmac, socket

theme = {
    "green": {
        "root": '#0f612f',
        "fg": '#39FF14',
        "primary": '#003928',
        "secondary": '#0a3e1e'
    },
    "dark_blue": {
        "root": '#445469',
        "fg": '#519aba',
        "primary": '#090b10',
        "secondary": '#0f111a'
    },
    
}

buttons = {
    0: [['CMD', 'start cmd /k cd /d %USERPROFILE%\Desktop'], ['Bash', 'start bash'], ['Python', 'start python'], ['Node', 'start node']],
    1: [['Browser', 'google.com'], ['Github', 'github.com'], ['Youtube', 'youtube.com'], ['Spotify', 'open.spotify.com']],
    2: [['Gmail', 'mail.google.com'], ['Docs', 'docs.new'], ['Sheets', 'sheets.new'], ['Slides', 'slides.new']],
    3: [['Instagram', 'instagram.com'], ['Reddit', 'reddit.com'], ['Whatsapp', 'web.whatsapp.com'], ['Linkedin', 'linkedin.com']],

}

menus = {
    "System": [ ["Win EXplorer", "start explorer"],
                ["Calculator", "start calc"],
                ["Notepad", "start notepad"],
                ["Paint", "start mspaint"], "---",

                ["Task Manager", "start taskmgr"],
                ["Control Panel", "start control"],
                ["Registry Editor", "start regedit"], 
                ["Disk Management", "start diskmgmt"]],

    "Network": [["Ping", "ping google.com"], 
                ["DNS Flush", "ipconfig /flushdns"], 
                ["IP details", " ipconfig"],
                ["TCP/IP Status", " netstat"]],

    "Advanced": [["Powershell", "start powershell"], 
                ["Bash", "start bash"], "---",

                ["System Info", " systeminfo"], 
                ["Environment Variables", " set"], 
                ["Available Drivers", " driverquery"]]
    
}

NOUNS = ['fishbowl', 'chairman', 'vineyard', 'caretaker', 'carwash', 'inland', 'barnyard', 'because', 'password', 'fireman', 'worldwide', 'buttercup', 'quicksand', 'courthouse', 'workshop', 'dustpan', 'backfield', 'bobcat', 'ratline', 'background', 'bathroom', 'rawboned', 'grapefruit', 'aircraft', 'talebearer',
 'tapeworm', 'crackpot', 'rattlesnake', 'courtroom', 'rearward', 'teaspoon', 'became', 'countermeasure', 'passbook', 'earthworm', 'countdown', 'copycat', 'lifetime', 'cartwheel', 'stonewall', 'checkmate', 'carport', 'bedbug', 'airfield', 'passkey', 'taleteller', 'candid', 'ladybug', 'stepson', 'bedclothes',
 'outdoors', 'drawstring', 'cutthroat', 'rawhide', 'armchair', 'hallway', 'crossbeam', 'lifeblood', 'lifeboat', 'darkroomṇ', 'caveman', 'counterpoise', 'redcoat', 'earache', 'baseball', 'gateway', 'rearmost', 'reddish', 'oatmeal', 'jigsaw', 'fourteen', 'standpipe', 'carefree', 'earring', 'mealtime', 'eyebrow',
 'earphone', 'chopstick', 'courtyard', 'stickup', 'yourself', 'flashback', 'cardsharp', 'pancake', 'greenhouse', 'kneecap', 'keyhole', 'seashell', 'backfire', 'dishwasher', 'ratsbane', 'starfish', 'crybaby', 'firefly', 'lifesaver', 'drawbridge', 'readywitted', 'eggplant', 'handgun', 'eyeball', 'candlelight', 'notebook',
 'household', 'lifework', 'steamship', 'airbrush', 'raincoat', 'cheesecloth', 'heartbeat', 'carrack', 'rattletrap', 'backbreaker', 'elsewhere', 'eyelid', 'darkroom', 'carpool', 'railway', 'carsick', 'handcuff', 'cancan', 'crybaby', 'grasshopper', 'together', 'rainbow', 'armpit', 'backlash', 'iceberg', 'airlift',
 'eardrum', 'waistline', 'bulldog', 'aftermath', 'nightmare', 'catfish', 'drainpipe', 'briefcase', 'butterfly', 'carryall', 'rainwater', 'Cannot', 'afternoon', 'candlestick', 'teardrop', 'scarecrow', 'cattail', 'rearrange', 'firefly', 'undermine', 'become', 'bedtime', 'wallpaper', 'clockwork', 'carpetbagger',
 'earthquake', 'stockroom', 'driveway', 'footprint', 'backdrop', 'drumstick', 'counteroffensive', 'daredevil', 'cardboard', 'landslide', 'billboard', 'foolproof', 'marketplace', 'steamboat', 'endless', 'breakfast', 'sailboat', 'driftwood', 'cowboy', 'daydream', 'Passover', 'redcap', 'brainstorm']

ADJECTIVES = ['adorable', 'adventurous', 'aggressive', 'agreeable', 'alert', 'alive', 'amused', 'angry', 'calm', 'careful', 'cautious', 'charming', 'cheerful', 'clean', 'clear', 'clever', 'cloudy', 'clumsy', 'eager', 'easy', 'elated', 'elegant', 'embarrassed', 'enchanting', 'encouraging', 'bad', 'beautiful', 'better',
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

WELCOME_RECURSIVE = """
Good day, {}
.
.
Quote of the day:

{}

- {}
""".format('-'.join([random.choice(ADJECTIVES), random.choice(NOUNS)]),
            requests.get(QUOTE_API).json()['content'], 
            requests.get(QUOTE_API).json()['author'])

WELCOME_START = """
Hello there, {}
I hope you have a good day.
""".format('-'.join([random.choice(ADJECTIVES), random.choice(NOUNS)]))

FUN = """
Did you know,
{}

"""

MISC = """
CPU Usage: {} %

Memory: {} %

{}: {:.1f} %

Battery: {} % ({})
"""

NETWORK = """
Public IP: {}

Private IP: {}

MAC Addr: {}
""".format(PUB_IP, PRI_IP, MAC)