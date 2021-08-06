import  os, webbrowser, requests

from tkinter import messagebox
from helpers.constants import *
import subprocess as sp

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

def universal_callback(command=None, http=None):
    if command:
        if command.startswith('start'):
            os.system("{}".format(command))

        if command.startswith('subprocess'):
            process = command.split(' ', 1)[-1]
            response = sp.getoutput(process)
            return response
    
    if http:
        if http.startswith('url'):
            http = http.split(' ', 1)[-1]
            webbrowser.get('edge').open(http)
        
        if http.startswith('request'):
            url = http.split(' ', 1)[-1]

            if url == 'quote':
                response = requests.get(QUOTE_API).json()
                return "{} \n\n- {}".format(response['content'], response['author'])

            if url == 'fact':
                response = requests.get(FACTS_API).json()
                return "Did you know, \n\n{}".format(response['text'])

            if url == 'poem':
                response = random.choice(requests.get(POEMS_API).json())
                return "{} \n\n{} \n\nBy {}".format(response['title'], response['content'], response['poet']['name'])

            if url == 'insult':
                response = requests.get(INSULT_API).json()
                return "{}".format(response['insult'])

            if url == 'kanye':
                response = requests.get(KANYE_API).json()
                return "Kanye REST once said, \n\n*{}*".format(response['quote'])

def about():
    messagebox.showinfo('About', ABOUT)

def destroy(root):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()