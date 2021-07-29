import  os, webbrowser

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def cmd():
    os.system("start cmd")

def bash():
    os.system("start bash")

def powershell():
    os.system("start powershell")

def universal(url=None):
    if url:
        if '.' in url:
            webbrowser.get('edge').open(url)
        else:
            os.system("start {}".format(url))
    

def browser():
    webbrowser.get('edge').open('http://www.google.com')

def github():
    webbrowser.get('edge').open('http://www.github.com')

def youtube():
    webbrowser.get('edge').open('http://www.youtube.com')


def gdocs():
    webbrowser.get('edge').open('docs.new')

def gsheets():
    webbrowser.get('edge').open('sheets.new')

def gslides():
    webbrowser.get('edge').open('slides.new')


def insta():
    webbrowser.get('edge').open('http://www.instagram.com')

def reddit():
    webbrowser.get('edge').open('http://www.reddit.com')

def linkedin():
    webbrowser.get('edge').open('http://www.linkedin.com')