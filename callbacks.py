import  os, webbrowser

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def universal_callback(url=None):
    if url:
        if ' ' in url:
            os.system("{}".format(url))
        else:
            webbrowser.get('edge').open(url)
